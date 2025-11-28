'''n=int(input("enter a value:"))
i=1
while i<=n:
    print(i)
    i+=1'''

'''n=int(input("enter a number"))
i=1
while i<=n:
    if i%2 == 0:
        print(i)
    i+=1'''

'''n=int(input("Enter a number:"))
i=0
while i<n:
    if not(i%2 == 0):
        print(i)
    i+=1'''

'''n=int(input("enter a number:"))
i=1
while i<=n:
    if not(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1'''

'''#building the multiplication table
for i in range():
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")'''

'''n= int(input("enter a number:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1'''

'''n=int(input("enter a value"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1'''

'''n= int(input("enter a value:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")'''

'''#factorial of number
n=int(input("enter a number:"))
factorial=1
while n>0:
    factorial = factorial*n
    n-=1
print(factorial)'''

'''n=int(input("enter a number:"))
factorial=1
for i in range(1,1+n):
    factorial=factorial*i
    print(factorial)'''


'''candies = 10
for i in range(candies):
    print("give to your friend")
    if candies -i ==5:
        print("i have only 5 candies left,stop now")
        continue'''

n=int(input("enter a number:"))
factorial=1
while n>0:
    factorial=factorial*n
    n-=1
    print(factorial)