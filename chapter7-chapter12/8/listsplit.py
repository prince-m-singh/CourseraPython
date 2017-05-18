fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words=""
for line in fh:
   # word=line.rstrip()
    words=line.rstrip().split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
            #print lst
    #lst.append(line.split())
    #print lst
lst.sort()
print lst

#print line.rstrip()
