print("1 add")
print("2 sub")
print("3 multi")
print("4 div")
a=int(input("enter the choice:"))
b=int(input("enter the no:"))
c=int(input("enter the no:"))

if a==1:
    x=b+c
    print(x)
elif a==2:
    x=b-c
    print(x)
elif a==3:
    x=b*c
    print(x)
elif a==4:
    x=b/c
    print(x)
else:
    print("error")
