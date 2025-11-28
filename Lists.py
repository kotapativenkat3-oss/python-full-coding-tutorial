# empty_list=[]
# number=[1,2,3,4]
# fruits=["apple","orange","jack fruit"]
# print(empty_list)
# print(number)
# print(fruits)

# k= [2,3,5,"apple","paali"]
# print(k[0])
# print(k[-1])
# print(k[3])
# print(k[4])

# a="hello world"
# print(a[::-1])
# print(a[:12])
# print(a[::2])

# l=[1,2,3]
# print(l[2])
# l.append(100)
# print(l)

#modifying the elements
# fruits=["apple","papaya","guava","grapes","pomogranate"]
# fruits[4]="sweerlemon"
# print(fruits)

#adding the elelment at last
# l=[1,2,3,4]
# l.append(5)
# print(l)

#inserting the element 
# l=[1,2,3,4]
# l.insert(2,5)
# print(l)

#remove element from anywhere in list
# l=[1,2,3,4]
# l.remove(4)
# l.remove(l[2])
# print(l)

#pop the element in last element in list
# l=[1,2,3,4]
# l.pop()
# print(l)

#getting the index
# l=[1,2,3,4,5,"pavan"]
# l.index("pavan")
# print(l)

#sorting the elements
# l=[5,8,6,7,4,2]
# l.sort()
# print(l)

# combining the lists
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# combined_list=list1+list2
# concat=list1[3]+list2[0]
# print(combined_list)
# print(concat)

# list comprehensions
# l1=[x**3 for x in range(1,4)]
# print(l1)

# a,b=input("enter a number:").split(",")
# x=int(a)
# y=int(b)
# print(type(x))
# print(type(y))

#1 2 3 5 6 7

# inp = input().split()
# l=[(int(item))**2 for item in inp]
# print(l)

# inp=input("enter a number:").split()
# l=[int(item)**2 for item in inp]
# print(l)

#sum of elements in list
# l=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# i=0
# length=len(l)
# while i<length:
#     sum=sum+l[i]
#     i+=1
# print(sum)
# print(length)

# l=[10,20,30,40,50]
# sum=0
# for i in l:
#     sum=sum+i
#     print(sum)

#printing max and min value in lists

# l=[2,5,6,15,8,25]

# l.sort()
# max=l[0]
# min=l[0]

# # for i in l:
# #     if i>max:
# #         max=i
# #     if i<min:
# #         min=i
# print(l)

inp=input().split()

l=[int(item) for item in inp]

new_l=[]

for i in l:
    if i in new_l:
        continue
    else:
        new_l.append(i)
print(new_l)