weather=input("Enter the weather condition:")
time_of_day=input("Enter the time of the day:")
if weather=="sunny":
    if time_of_day=="morning":
        print("play cricket")
elif weather=="rainy" :
    if time_of_day=="afternoon":
        print("play football")
elif weather=="cloudy" and time_of_day=="midnight":
    print("play checkers")
elif weather=="snowy" and time_of_day=="midday":
    print("play chess")
else:
    print("do nothing")
