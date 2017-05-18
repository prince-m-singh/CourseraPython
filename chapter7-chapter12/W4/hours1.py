hrs = raw_input("Enter Hours:")
h = float(hrs)
rate=raw_input("Enter Rate:")
r=float(rate)
if(hrs<=40):
    pay=h*r
else:
    pay=40*r
    pay2=(h-40)*(1.5*r)
    pay=pay+pay2
print pay,pay2