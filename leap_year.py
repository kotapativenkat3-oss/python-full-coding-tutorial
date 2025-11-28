year = int(input("Enter a year: "))

leap  =False

if year%100 == 0 and year%400 == 0:
    leap_year = True
elif year%4 == 0 and year%100 !=0:
    leap_year = True
else:
    leap_year = False
    
print(leap_year)