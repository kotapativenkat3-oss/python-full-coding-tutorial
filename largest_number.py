a=input()

x,y,z=a.split(",")
num1=int(x)
num2=int(y)
num3=int(z)
great = 0
if num1 > num2:
    if num1 > num3:
        print(num1,"is largest")
    else:
        print(num1,"is smaller")
if num2 > num1:
    if num2 > num3:
        print(num2,"is largest")
    else:
        print(num2,"is smaller")
if num3 > num1:
    if num3 > num2:
        print(num3,"is largest")
    else:
        print(num3,"is smaller")
if num1 and num2==num3:
    print("all are equal")