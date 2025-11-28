#a,b,c
#a,b,c
#finding roots of quadratic equation
def caluclate_roots(a,b,c):
    root1=0
    root2=0
    d=(b**2)-4*a*c
    root1=(-b+(d**(0.5)))/2*a
    root2=(-b-(d**(0.5)))/2*a
    print(f"root1:{root1},root2:{root2}")
a=(int(input("Enter a value:")))
b=(int(input("Enter b value:")))
c=(int(input("Enter c value:")))
caluclate_roots(a,b,c)

# a=(int(input("Enter a value:")))
# b=(int(input("Enter b value:")))
# c=(int(input("Enter c value:")))
# root1=0
# root2=0
# d=(b**2)-4*a*c
# root1=(-b+(d**(0.5)))/2*a
# root2=(-b-(d**(0.5)))/2*a
# print(f"root1:{root1},root2:{root2}")