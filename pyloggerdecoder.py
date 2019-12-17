

coded=open("pyloggercoded.txt",'r')
val=coded.read()
val=val.rstrip("\n")

newList=val.split("\n")
randomInteger=newList[0]

newString=""
newrandomInteger=int(newList[0])
for i in range(1,len(newList)):
    newString=newString+str(chr(int(newList[i])-newrandomInteger))
   
exec(newString)

