import random
import os

filename=raw_input("Enter python file name...")
coded=open(filename+"coded.txt",'a')
file= open(filename+".py","r")
line=file.read()

randomInteger=random.randint(1,1000)
print(randomInteger)
coded.write(str(randomInteger)+"\n")
asciiList=[]

for i in line:
        asciiList.append(str(ord(i)+randomInteger))

for i in asciiList:
        coded.write(i+"\n")

coded.close()
file.close()

file1=open(filename+"decoder.py",'w')

s = """

coded=open(\""""+filename+"coded.txt" """",'r')
val=coded.read()
val=val.rstrip("\\n")

newList=val.split("\\n")
randomInteger=newList[0]

newString=""
newrandomInteger=int(newList[0])
for i in range(1,len(newList)):
    newString=newString+str(chr(int(newList[i])-newrandomInteger))
   
exec(newString)

"""


file1.write(s)
file1.close()
