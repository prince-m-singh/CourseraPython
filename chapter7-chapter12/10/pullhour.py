name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lst=list()
count=dict()

handle = open(name)
#count = 0
for line in handle:
     if line.startswith("From") and not line.startswith("From:") :
       
        word=line.rstrip().split()
        #print word
        time=word[5]
        hour=time.split(":")
        lst.append(hour[0])
        #print lst
        
        
for number in lst:
    count[number]=count.get(number,0)+1
        
    #count=count+1
#print count
lst=list()
for key,val in count.items():
    lst.append((key,val))
lst.sort()
for key,val in lst:
    print key,val