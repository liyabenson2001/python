#roots of quadratic equation
a=int(input("enter the no:"))
b=int(input("enter the no:"))
c=int(input("enter the no:"))
r=b*b-4*a*c
if r>0:
    print("the roots are 2")
elif r==0:
    print("there is 1 root:")
else:
    print("no roots")
    
