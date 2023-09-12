n=int(input("enter the no:"))
sum=0
step=1
condition=True
while condition:
    while n:
        sum+=n%10
        n=n//10
    print("step",sum)
    n=sum
    sum=0
    step+=1
    condition=n>9



