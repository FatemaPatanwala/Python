def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")