fname = raw_input("Enter the file name: ")
fh=open(fname)
for line in fh:
    line=line.rstrip().upper()
    print line
#print fh