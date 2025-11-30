# import sys
# sys.setrecurrsionlimit(10)
# i=0
# def greet():
#     global i
#     i+=1
#     print("hello", i)
#     greet()
# greet()


# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)


# result=fact(4)
# print(result)

# def fact(m):
#     if m==0:
#         return 1
#     return m*fact(m-1)
# restlt=fact(5)
# print(restlt)

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result=fact(5)
# print(result)

def fibb(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fibb(5)