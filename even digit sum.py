n=int(input("enter the no:"))
sum=0
while n!=0:
    d=n%10
    if d%2==0:
        sum=sum+d
    n=n//10
print("sum of even no is:",sum)

