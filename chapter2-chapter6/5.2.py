maximum=0
minimum=None
average=0
while True:
    try:
        line = raw_input('>Enter a number: ')
        if line == 'done':
            break
        num=int(line)
        if(num>maximum):
            maximum=num
        elif(minimum>num or minimum is None):
            minimum=num
    except:
        print("Invalid number")
print maximum
print minimum
