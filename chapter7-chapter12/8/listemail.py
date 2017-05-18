fname = raw_input("Enter file name: ")
lst=list()
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From:") :
        email=line.rstrip().split()
        print email[1]
        count=count+1
        #if email[1] not in lst:
        #    lst.append(email[1])
    


print "There were", count, "lines in the file with From as the first word"
#print lst