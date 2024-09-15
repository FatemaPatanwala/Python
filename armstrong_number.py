a=int(input("Enter a number"))
x=a
temp=a
new=0
num=0

while temp>0:
    num=num+1
    temp=temp//10


while a>0:
    b=a%10
    new=new+b**num
    a=a//10
if x==new:
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")


