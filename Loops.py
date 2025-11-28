# k=9
# while k<15:
#     print("hi ",k)
#     k+=1

# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")

# candies = 20
# if candies >10:
#     print("give to your friend")
# else:
#     print("i don't have candies")

# c=int(input("enter a number of candies:"))
# while c>0:
#     print("give candy to your friend")
#     c-=1
# if c==0:
#     print("no more candies")

# c=int(input("enter a number of candies:"))
# for i in range(0,c):
#     print("give candy to your friend")

# a = "hello world!!"
# for i in a:
#     print(i)

# m="hello world!!"
# for i in range(len(m)):
#     print(m[i])

# m=int(input("enter no of candies:"))
# for i in range(m):
#     print("give candy to your friend")
#     if m-i == 10:
#         print(f"i have only {m-i} candies left")
#         break


# candies=int(input("enter no of candies:"))
# for i in range(candies):
#     print("give candy to your friend")
#     if candies - i == 20:
#         print(f"i have only {candies - i} candies left")
#         break

# candies = int(input("enter no of candies:"))
# for i in range(candies):
#     print("give to your friend")
#     if candies - i == 5:
#         print("give 5th candy to your special friend")
#         continue
#     print(f"candies left: {candies-i}")

# candies = int(input("enter no of candies:"))
# for i in range(candies):
#     print("give candy to your friend")
#     if candies - i == 4:
#         print("give 4th special candy to your friend")
#         continue
#     elif candies - i == 3:
#         print("give 3rd chocolate to your girl friend")
#         break
#     print(f"candies left: {candies - i}")

# n=int(input("enter a number:"))
# while n<=5 and n>0:
#     print(n)
#     n+=1

# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(i)
#     i+=1

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print(i)

# n=int(input("enter a number:"))
# for i in range(0,n+1):
#     print(i)

# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     print(i)
#     i+=1

# n=int(input("enter a  number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     print(sum)
#     i+=1

# n=int(input("enter a number:"))
# i=1
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     print(sum)

# n=int(input("enter a number:"))
# i=0
# for i in range(1,n+1,2):
#     print(i)

# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1

# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     if not (i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# n=int(input("enter a number:"))
# i=1
# sum=0
# for i in range(1,n+1):
#     sum+=i
#     print(sum)
#     i+=1

# n=int(input("enter a number:"))
# i=1
# for i in range(1,1+n,2):
#     print(i)
#     i+=1

# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(f"{n}x{i}={n*i}")
#     i+=1

# n=int(input("enter a number"))
# i=1
# while i<=10:
#     print(f"{n}x{i}={n*i}")
#     i+=1

# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")


# n=int(input("enter a number:"))
# factorial=1
# while n>0:
#     factorial=factorial*n
#     n-=1
# print(factorial)

# n=int(input("enter a number:"))
# factorial=1
# while n>0:
#     factorial=factorial*n
#     n-=1
# print(factorial)

# n=int(input("enter no of candies"))
# i=0
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     print(sum)
#     i+=1

# i=int(input("enter a value:"))
# fact=1
# for i in range(1,i+1):
#     fact=fact*i
#     print(fact)

# def employee_info(name,profession,mode,age):
#     print(f"name:{name}")
#     print(f"age:{age}")
#     print(f"mode:{mode}")
#     print(f"profession:{profession}")
# employee_info(name="pavan",age=21,profession="engineer",mode="permenant")