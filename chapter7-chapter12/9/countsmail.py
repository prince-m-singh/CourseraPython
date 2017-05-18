name = raw_input("Enter file:")
lst=list()
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
count = 0
for line in handle:
     if line.startswith("From:") :
        email=line.rstrip().split()
        fromemail=email[1]
        lst.append(fromemail)
        #print email[1]
        
        count=count+1
        #if email[1] not in lst:
        #    lst.append(email[1])
#print lst
#print "There were", count, "lines in the file with From as the first word"

count = dict()
for word in lst:
    count[word]=count.get(word,0)+1
bigcount = None
bigword = None
for word,number in count.items():
    if bigcount is None or number >bigcount:
        bigword=word
        bigcount=number
print bigword , bigcount
print count
