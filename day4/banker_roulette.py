import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random.shuffle(names)
print(f"{names[0]} is going to buy the meal today!")

