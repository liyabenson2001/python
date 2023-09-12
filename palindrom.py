n=int(input("enter the no:"))
t=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("rev no",rev)
if rev==t:
    print("yes")
else:
    print("no")
