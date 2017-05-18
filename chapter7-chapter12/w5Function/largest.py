largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        number=int(num)
        if largest is None or  number>largest: largest=number
        if smallest is None or smallest>number: smallest=number
    except:
        print "Invalid Input"
    #print number

print "Maximum", largest, smallest