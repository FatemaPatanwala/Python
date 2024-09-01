a=input("Enter a string : ").lower()
b=input("Enter another string : ").lower()

x=sorted(a)
y=sorted(b)

if x==y:
    print("Both sentences are anagram")
else:
    print("Both are not anagram")
