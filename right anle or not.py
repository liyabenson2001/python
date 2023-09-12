a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))
if a*a+b*b==c*c:
    print("the triangle is right angled")
elif c*c+b*b==a*a:
    print("the triangle is right angled")
elif a*a+c*c==b*b:
    print("the triangle is right angled")
else:
    print("the triangle is not right angled")
      
