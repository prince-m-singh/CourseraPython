import re

name = raw_input("Enter file:")
handle = open(name)
numlist=list()
for line in handle:
    line =line.rstrip()
    number=re.findall('[0-9]+',line)
    if len(number) <=0: continue
 #   print number
    numlist=numlist+number
    #numlist.append(number)
#print numlist
b=sum((int)(i) for i in numlist)
print b