import os,glob,subprocess,pytz
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
from tzlocal import get_localzone 
local_tz = pytz.timezone(str(get_localzone()))

from SharedData.Metadata import Metadata
from SharedData.Logger import Logger
from SharedData.AWSKinesis import KinesisLogStreamConsumer,KinesisStreamProducer

class RoutineScheduler:

    def __init__(self,stream_name):
        self.consumer = KinesisLogStreamConsumer()
        self.producer = KinesisStreamProducer(stream_name)

    def LoadSchedule(self,schedule_name):
        self.schedule=[]        

        today = datetime.now().date()
        year = today.timetuple()[0]
        month = today.timetuple()[1]
        day = today.timetuple()[2]        

        _sched = Metadata('SCHEDULES/'+schedule_name).static.reset_index()
        sched = pd.DataFrame()
        for i,s in _sched.iterrows():
            runtimes = s['Run Times'].split(',')
            for t in runtimes:
                hour = int(t.split(':')[0])
                minute = int(t.split(':')[1])
                dttm = local_tz.localize(datetime(year,month,day,hour,minute))
                s['Run Times'] = dttm
                sched = sched.reindex(columns=s.index.union(sched.columns))
                sched = pd.concat([sched, pd.DataFrame(s).T])

        sched = sched.sort_values(by=['Run Times','Name']).reset_index(drop=True)
        sched['Status'] = np.nan
        sched['Last Message'] = np.nan
        sched['index'] = [s.lower().replace('\\','/') for s in sched['index']]
        sched.loc[sched['Dependencies'].isnull(),'Dependencies'] = ''
        sched['Dependencies'] = [s.lower().replace('\\','/') for s in sched['Dependencies']]


        uruntimes = sched['Run Times'].unique()
        runtime = uruntimes[0]
        sched_sort = pd.DataFrame(columns=sched.columns)
        for runtime in uruntimes:
            # mark pending routines
            while True:
                idx = runtime.astimezone(tz=local_tz)>=sched['Run Times']
                idx = (idx) & ((sched['Status'].isnull()) | (sched['Status']=='WAITING DEPENDENCIES'))

                dfpending = sched[idx]
                expiredidx = dfpending.duplicated(['Computer','Script'],keep='last')
                if expiredidx.any():
                    expiredids = expiredidx.index[expiredidx]
                    sched.loc[expiredids,'Status'] = 'EXPIRED'
                dfpending = dfpending[~expiredidx]
                i=0
                for i in dfpending.index:
                    r = dfpending.loc[i]
                    if (not str(r['Dependencies'])=='') & (not str(r['Dependencies'])=='nan'):
                        run=True
                        sched.loc[i,'Status'] = 'WAITING DEPENDENCIES'
                        dependencies = r['Dependencies'].replace('\n','').split(',')                
                        for dep in dependencies:                            
                            idx = sched['index']==dep
                            idx = (idx) & (sched['Run Times']<=runtime.astimezone(tz=local_tz))                            
                            ids = sched.index[idx]
                            if len(ids)==0:
                                # Logger.log.info('Dependency not scheduled for '+r['Computer']+':'+r['Script'])
                                Logger.log.error('Dependency not scheduled for '+r['Computer']+':'+r['Script'])
                                raise Exception('Dependency not scheduled for '+r['Computer']+':'+r['Script'])
                            else:
                                if not str(sched.loc[ids[-1],'Status']) == 'COMPLETED':
                                    run=False
                        if run:
                            sched.loc[i,'Status'] = 'PENDING'
                    else:
                        sched.loc[i,'Status'] = 'PENDING'

                idx = sched['Status']=='PENDING'
                if idx.any():
                    sched_sort = pd.concat([sched_sort, sched[idx]])
                    sched_sort['Status'] = np.nan
                    sched.loc[idx,'Status'] = 'COMPLETED'
                else:
                    break

        self.schedule = sched_sort
        return sched_sort

    def UpdateRoutinesStatus(self):
        sched = self.schedule                
        local_tz = pytz.timezone(str(get_localzone()))
        # RefreshLogs
        dflogs = self.consumer.readLogs()
        if not dflogs.empty:
            dflogs['index'] = dflogs['user_name']+':'+dflogs['logger_name']
            dflogs['index'] = [s.lower().replace('\\','/') for s in dflogs['index']]

            dflogs = dflogs[dflogs['asctime'].notnull()].copy()
            dflogs['asctime'] = pd.to_datetime(dflogs['asctime'])
            dflogs['asctime'] = [dt.astimezone(tz=local_tz) for dt in dflogs['asctime']]

            i=0
            for i in sched.index:
                r = sched.loc[i]
                idx = dflogs['index']==r['index']
                idx = (idx) & (dflogs['asctime']>=r['Run Times'])    
                if np.any(idx):    
                    sched.loc[i,'Last Message'] = dflogs[idx].iloc[-1]['message']   

                                
            dferr = dflogs[dflogs['message']=='ROUTINE ERROR!']
            dferr = dferr.reset_index(drop=True).sort_values(by='asctime')
            i=0
            for i in dferr.index:
                r = dferr.iloc[i]
                idx = sched['index']==r['index']
                idx = (idx) & (r['asctime']>=sched['Run Times'])
                if idx.any():
                    ids = idx[::-1].idxmax()
                    sched.loc[ids,'Status'] = 'ERROR'
                    idx = sched.loc[idx,'Status'].isnull()
                    idx = idx.index[idx]
                    sched.loc[idx,'Status'] = 'EXPIRED'

            compl = dflogs[dflogs['message']=='ROUTINE COMPLETED!'].reset_index(drop=True).sort_values(by='asctime')
            i=0
            for i in compl.index:
                r = compl.iloc[i]
                idx = sched['index']==r['index']                
                idx = (idx) & (r['asctime']>=sched['Run Times'])
                if idx.any():
                    ids = idx[::-1].idxmax()
                    sched.loc[ids,'Status'] = 'COMPLETED'
                    idx = sched.loc[idx,'Status'].isnull()
                    idx = idx.index[idx]
                    sched.loc[idx,'Status'] = 'EXPIRED'

        # mark pending routines
        idx = datetime.now().astimezone(tz=local_tz)>=sched['Run Times']
        idx = (idx) & ((sched['Status'].isnull()) | (sched['Status']=='WAITING DEPENDENCIES'))
        
        dfpending = sched[idx]
        expiredidx = dfpending.duplicated(['Computer','Script'],keep='last')
        if expiredidx.any():
            expiredids = expiredidx.index[expiredidx]
            sched.loc[expiredids,'Status'] = 'EXPIRED'
        
        dfpending = dfpending[~expiredidx]
        for i in dfpending.index:
            r = dfpending.loc[i]
            if (not str(r['Dependencies'])=='') & (not str(r['Dependencies'])=='nan'):
                run=True
                sched.loc[i,'Status'] = 'WAITING DEPENDENCIES'
                dependencies = r['Dependencies'].replace('\n','').split(',')                
                for dep in dependencies:                    
                    idx = sched['index']==dep                    
                    idx = (idx) & (sched['Run Times']<=datetime.now().astimezone(tz=local_tz))
                    ids = sched.index[idx]
                    if len(ids)==0:                        
                        Logger.log.error('Dependency not scheduled for '+r['Computer']+':'+r['Script'])
                    else:
                        if not str(sched.loc[ids[-1],'Status']) == 'COMPLETED':
                            run=False
                if run:
                    if sched.loc[i,'Run']:
                        sched.loc[i,'Status'] = 'PENDING'
                    else:
                        sched.loc[i,'Status'] = 'PENDING EXTERNAL'
            else:
                if sched.loc[i,'Run']:
                        sched.loc[i,'Status'] = 'PENDING'
                else:
                    sched.loc[i,'Status'] = 'PENDING EXTERNAL'                
        
        self.schedule=sched
        return sched

    def RunPendingRoutines(self):   
        sched = self.schedule
        
        # Run pending routines
        dfpending = sched[sched['Status']=='PENDING']

        for i in dfpending.index:
            r = dfpending.loc[i].copy()
            if str(r['Last Message'])=='nan':
                target = r['Computer']
                
                if '#' in r['Script']: # has branch
                    branch = r['Script'].split('/')[0].split('#')[-1]
                    repo = r['Script'].split('/')[0].split('#')[0]
                    routine = r['Script'].replace(repo,'').\
                        replace('#','').replace(branch,'')[1:]+'.py'
                else:
                    branch=''
                    repo = r['Script'].split('/')[0]
                    routine = r['Script'].replace(repo,'')[1:]+'.py'
                                    
                data = {
                    "sender" : "MASTER",
                    "job" : "routine",
                    "target" : target,        
                    "repo" : repo,
                    "routine" : routine
                }
                if branch != '':                    
                    data['branch']=branch

                if 'args' in r:
                    r['args'] = str(r['args'])
                    if (r['args']!='') & (r['args']!='nan'):
                        data['args']=r['args']

                self.producer.produce(data,'command')
                sched.loc[r.name,'Status'] = 'RUNNING'
                Logger.log.info('Command to run %s:%s sent!' % (target,r['Script']))
        
        self.schedule = sched
        return sched



