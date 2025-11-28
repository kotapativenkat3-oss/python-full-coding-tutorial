num1=int(input("Enter num1 number:"))
num2=int(input("Enter num2 number:"))
operator=input("Enter operator:")
if operator == "+":
    print(f"the sum:{num1+num2}")
elif operator == "-":
    print(f"the difference:{num1-num2}")
elif operator == "*":
    print(f"the multiplication:{num1*num2}")
elif operator == "/":
    print(f"the division:{num1/num2}")
else:
    print("invalid operator")