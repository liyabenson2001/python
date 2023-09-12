n=int(input("enter the no:"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
if sum>9:
    n=sum
print("sum is",sum)

