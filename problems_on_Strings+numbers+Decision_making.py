#s=input("enter a word:")
#f1=s.lower()
#a=f1.count('a')
#e=f1.count('e')
#i=f1.count('i')
#o=f1.count('o')
#u=f1.count('u')

#print(f"no:of vowel:{a+e+i+o+u}")

##Grade calculator

M=int(input("Enter marks in maths:"))
C=int(input("Enter marks in chemistry:"))
E=int(input("Enter marks in English:"))
S=int(input("Enter marks in Social:"))

Total_marks=M+C+E+S
average=Total_marks/4

percentage=(Total_marks/400)*100

if percentage>=90 and percentage<=95:
    print("Grade A")
elif percentage>=80 and percentage<90:
    print("Grade B")
elif percentage>=70 and percentage<80:
    print("Grade C")
else:
    print("Grade D")

print(f"Total marks:{Total_marks} \nAverage:{average} \nPercentage:{percentage}")