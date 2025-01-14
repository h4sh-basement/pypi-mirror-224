import os,sys
import logging
import boto3
from pathlib import Path
from datetime import datetime, timedelta
import glob
import pandas as pd
from pythonjsonlogger.jsonlogger import JsonFormatter
import boto3


from SharedData.AWSKinesis import KinesisLogStreamHandler

class Logger:

    log = None
    user = 'guest'
    source = 'unknown'

    @staticmethod
    def connect(source,user=None):
        if Logger.log is None:
            if 'SOURCE_FOLDER' in os.environ:
                try:
                    commompath = os.path.commonpath([source,os.environ['SOURCE_FOLDER']])
                    source = source.replace(commompath,'')
                except:
                    pass
            elif 'USERPROFILE' in os.environ:
                try:
                    commompath = os.path.commonpath([source,os.environ['USERPROFILE']])
                    source = source.replace(commompath,'')
                except:
                    pass
            
            finds = 'site-packages'
            if finds in source:
                cutid = source.find(finds) + len(finds) + 1
                source = source[cutid:]            
            source = source.replace('Windows\\system32\\','')
            source = source.lstrip('src').lstrip('\\src')
            source = source.lstrip('\\').lstrip('/')        
            source = source.replace('.py','')
            Logger.source = source
            
            if not user is None:                
                Logger.user = user
                        
            path = Path(os.environ['DATABASE_FOLDER'])
            path = path / 'Logs'
            path = path / datetime.now().strftime('%Y%m%d')
            path = path / (os.environ['USERNAME']+'@'+os.environ['COMPUTERNAME'])        
            path = path / (source+'.log')
            if not path.parents[0].is_dir():
                os.makedirs(path.parents[0])
            os.environ['LOG_PATH'] = str(path)

            if 'LOG_LEVEL' in os.environ:
                if os.environ['LOG_LEVEL']=='DEBUG':
                    loglevel = logging.DEBUG
                elif os.environ['LOG_LEVEL']=='INFO':
                    loglevel = logging.INFO   
            else:
                loglevel = logging.INFO

            # Create Logger
            Logger.log = logging.getLogger(source)
            Logger.log.setLevel(logging.DEBUG)    
            formatter = logging.Formatter(os.environ['USERNAME']+'@'+os.environ['COMPUTERNAME'] + 
                ';%(asctime)s;%(name)s;%(levelname)s;%(message)s',\
                datefmt='%Y-%m-%dT%H:%M:%S%z')
            #log screen
            handler = logging.StreamHandler()
            handler.setLevel(loglevel)    
            handler.setFormatter(formatter)
            Logger.log.addHandler(handler)
            # #log file        
            # fhandler = logging.FileHandler(os.environ['LOG_PATH'], mode='a')
            # fhandler.setLevel(loglevel)    
            # fhandler.setFormatter(formatter)
            # Logger.log.addHandler(fhandler)
            #log to aws kinesis
            kinesishandler = KinesisLogStreamHandler(user=Logger.user)
            kinesishandler.setLevel(logging.DEBUG)
            jsonformatter = JsonFormatter(os.environ['USERNAME']+'@'+os.environ['COMPUTERNAME'] + 
                ';%(asctime)s;%(name)s;%(levelname)s;%(message)s',\
                datefmt='%Y-%m-%dT%H:%M:%S%z')
            kinesishandler.setFormatter(jsonformatter)
            Logger.log.addHandler(kinesishandler)            
            
        
    @staticmethod
    def readLogs(self):    
        logsdir = Path(os.environ['LOG_PATH']).parents[0]
        lenlogsdir = len(str(logsdir))
        files = glob.glob(str(logsdir) + "/**/*.log", recursive = True)   
        df = pd.DataFrame()
        # f=files[0]
        for f in files:
            source = f[lenlogsdir+1:].replace('.log','.py')
            try:
                _df = pd.read_csv(f,header=None,sep=';',\
                    engine='python',on_bad_lines='skip')
                _df.columns = ['user','datetime','name','type','message']
                _df['source'] = source
                df = df.append(_df)
            except Exception as e:
                print('Read logs error:'+str(e))

        return df
