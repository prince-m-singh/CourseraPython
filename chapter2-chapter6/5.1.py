total=0
count=0
average=0
while True:
    try:
        line = raw_input('>Enter a number: ')
        if line == 'done':
            break
        num=int(line)
        total=total+num
        count=count+1
    except:
        print("Invalid number")
print total
print count
average=float(float(total)/float(count))
print average
