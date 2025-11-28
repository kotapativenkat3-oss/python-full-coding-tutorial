#Swapping the numbers without using third variable
#a=int(input("Enter a number:"))
#b=int(input("Enter b number:"))
#b=b+a
#a=b-a
#b=b-a
#print(f"value of a is: {a}")
#print(f"value of b is: {b}")

def swap_numbers(a,b):
    b=a+b
    a=b-a
    b=b-a
    print(f"the value of a is:{a}")
    print(f"the value of b is:{b}")
a=int(input("enter a number:"))
b=int(input("enter b number:"))
swap_numbers(a,b)

#converting temperature units
c=int(input("Enter the temperature in celcius:"))
f=c*(9/5)+32
k=273+c
print(f"temperature in fahrenheit id: {f}")
print(f"temperature in kelvin's scale is: {k}")