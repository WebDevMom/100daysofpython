#leap year
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    print("leap year.")
elif year % 100 == 0:
    print("not leap year.")
elif year % 400 == 0:
    print("leap year.")
else:
    print("not leap year")



 



#for every year that is evenly divible by 4 
#except every year that is evenly divisible by 100
#unless the year is also evenly divible by 400
#ex. year 2000
#2000/4 = 500 -leap
#2000/100 = 20 not leap
#2000/400 = 5 leap