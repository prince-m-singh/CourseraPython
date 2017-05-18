fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
addnum=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num=line.find(":")
    print num
    data=line[num+1:].strip()
    print type(data)
    print float(data)
    num1=float(data)
    addnum=addnum+num1
    count=count+1
    print line,count,addnum,addnum/count
    
print "Average spam confidence: "  +str(addnum/count)