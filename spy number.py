n=int(input("enter the no:"))
sum=0
mul=1
while n>0:
    sum+=n%10
    mul=mul*(n%10)
    n=n//10
if sum==mul:
    print("spy number")
else:
    print("not spy number")
