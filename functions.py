# def fun(a,b,c): #function defination
#     print("it is a function",a+b+c)
# fun(5,8,7) #function call

# def fun(*a): #function defination (* is for orbitary arguments)
#     print("this is function",a)
# fun(1,2,3) #function call

# def fun(**a): # (** is for keyword arguments)
#     print("this is a function",a)
# fun(a=1,b=2) #function call

#nested functions
# def order():
#     print("outer functions")
#     def inner():
#         print("inner functions")
#     inner()
# order()


# def add_numbers(a,b):
#     return(a+b)
# result=add_numbers(8,5)
# print(result)
# def sub_numbers(a,b):
#     return(a-b)
# file=sub_numbers(7,4)
# print(file)
# def mul_numbers(a,b):
#     return(a*b)
# luffy=mul_numbers(8,6)
# print(luffy)
# def div_numbers(a,b):
#     return(a/b)
# zoro=div_numbers(8,2)
# print(zoro)

# def add_numbers(a,b):
#     return a+b
# result=add_numbers(5,2)
# print(result)

# def employee_info(name,age,profession,maritalstatus):
#     print(f"name:{name}")
#     print(f"age:{age}")
#     print(f"profession:{profession}")
#     print(f"marital status:{maritalstatus}")
# employee_info(age="21",profession="engineer",maritalstatus="unmarried",name="pavan")

# def greet_user(name,greeting="Hello"):
#     return greeting + "," + name+"!"
# greeting1=greet_user("maki")
# greeting2=greet_user("paul","how do you do")
# print(greeting1)
# print(greeting2)

# def greet_man(name,greet="how do you do"):
#     return greet + ","+name+"!!"
# great1=greet_man("pavan")
# great2=greet_man("nayeem","hello how are you")

# print(great1)
# print(great2)

# def intro(name,intro="my name is "):
#     return intro + name+"!!"
# tin=intro("yuva swamy")
# bin=intro("chetan","how are you")
# print(tin)
# print(bin)


# def intro(name,greeting="how are you "):
#     return greeting+name+"!!"
# greet11=intro("karthik")
# greet12=intro("nagi","how do you do ")
# print(greet11)
# print(greet12)

# def add(a,b):
#     return a+b
# result=add(9,1)
# print(result)

# def intro(name,greeting="how are you!"):
#     return greeting + name + "!"
# greeting1=intro("pavan")
# greeting2=intro("samruth","how do you do man!")
# print(greeting1)
# print(greeting2)

# global_var = 15
# def my_function():
#     print(global_var)
# print(global_var)

# def add(a,b):
#     sum=a+b
#     print(sum)
# add(5,3)
# print(sum)

# global_vare = "16"
# def function():
#     print(global_vare)
# print(global_vare)

# def add(a,b):
#     sum=a+b
#     print(sum)
# add(8,2)
# print(sum)
# def sub(c,d):
#     sub=c-d
#     print(sub)
# sub(8,3)
# print(sub)

# def employee_info(name,profession,age,marital_status,courses):
#     print(f"name:{name}")
#     print(f"age:{age}")
#     print(f"courses:{courses}")
#     print(f"profession:{profession}")
#     print(f"marital_status:{marital_status}")
# employee_info(age="21",profession="engineer",marital_status="unmarried",courses="java,python",name="pavan")

# def greet(name,greeting="hi how do you do!"):
#     return greeting+name+"!"
# great1=greet("nayeem")
# great2=greet("charan","how are you")
# print(great1)
# print(great2)

# def add_numbers(a,b):
#     return(a+b)
# result=add_numbers(9,1)
# print(result)
# def sub_numbers(c,d):
#     return(c-d)
# diff=sub_numbers(11,1)
# print(diff)
# def mul_numbers(j,k):
#     return(j*k)
# combine=mul_numbers(2,5)
# print(combine)
# def div_numbers(l,m):
#     return(l/m)
# bin=div_numbers(20,2)
# print(bin)

# def add(a,b):
#     sum=a+b
#     print(sum)
# add(9,1)
# print(sum)


# def swap_numbers(a,b):
#     b=a+b
#     a=b-a
#     b=b-a
#     print(f"the value of a is:{a}")
#     print(f"the value of b is:{b}")
# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# swap_numbers(a,b)

# def greet():
#     print("hello")
#     greet()
# greet()

# def fibanocci(k):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,k):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibanocci(5)


# def add(a):
#     Area_of_circle=3.14*(a**2)
#     print(f"Area_of_circle:{Area_of_circle}")
# add(5)

def fibb(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        print(c)
fibb(5)

add=lambda x,y:x+y
result=add(5,8)
print(result)