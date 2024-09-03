a=int(input("Enter any number :"))

if a==1:
    print("Its not a prime number")
elif a>1:
    for i in range(2,a):
        if a%i==0:
            print("Its not a prime number")
            break 
    else:
        print("Its a prime number")
