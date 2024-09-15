a=int(input("Enter a number"))
new=0
while a>0:
    b=a%10
    new=new*10+b
    a=a//10
print(new)
