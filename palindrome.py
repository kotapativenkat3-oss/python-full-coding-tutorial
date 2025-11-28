s=input("enter a number:")
reverse = s[::-1]

if s == reverse:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

