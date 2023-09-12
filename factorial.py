n=int(input("enter the no:"))
sum=0
t=n
while n>0:
    i=1
    fact=1
    r=n%10
    while (i<=r):
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==t:
    print("strong number")
else:
    print("not a strong number")
