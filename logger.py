import openfile
import datetime
import os 

logFifeName = "logs.txt"

def log(logInfo):
    now = datetime.datetime.now()
    openfile.addline(logFifeName,str(now)+'--> '+str(logInfo)+'\n')

if __name__ == "__main__":
    log("hello")