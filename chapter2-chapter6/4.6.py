hours=int(raw_input("Enter Hours:"))
rate=int(raw_input("Enter Rate:"))
def computergrade(hours,rate):
    if(hours>40):
          pay=40*rate;
          hours=hours-40;
          pay=pay+(hours*1.5*rate)
    else:
          pay=hours*rate
    print(pay)
