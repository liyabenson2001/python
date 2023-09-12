#calculating elecricity bill
units=int(input("enter the no of unit:"))
if units<=100:
    x=units*1.5+25
    print("electricity bill:",x)
elif units<=200:
    x=((100*1.5)+(units-100)*2.5)+50
    print("electricity bill:",x)
elif units<=300:
    x=((100*1.5)+(100*2.5)+(units-200)*4)+75
    print("electricity bill:",x)
elif units<=350:
    x=((100*1.5)+(100*2.5)+(100*4)+(units-300)*5)+100
    print("electricity bill:",x)
else:
    x=1500
    print("electricity bill:",x)
    
