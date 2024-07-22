a=int(input("Enter the number :"))
b=int(input("Enter the number :"))


def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

add=sum(a,b)
sub=subtract(a,b)
mul=multiply(a,b)
div=divide(a,b)


c=int(input('''Enter the operation to be performed:
                1. Addition  
                2.Subtraction 
                3. Multipication 
                4. Division : '''))

if c==1:
    print(add)
elif c==2:
    print (sub)
elif c==3:
    print(mul)
elif c==4:
    print(div)