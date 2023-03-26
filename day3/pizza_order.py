print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
small_pizza_cost = 15
med_pizza_cost = 20
large_pizza_cost = 25
add_pepp_small_cost = 2
add_pepp_med_lg_cost = 3
add_extra_cheeese_cost = 1

if size == "S":
    bill += small_pizza_cost
    if add_pepperoni == "Y":
        bill += add_pepp_small_cost
elif size == "M":
    bill += med_pizza_cost
    if add_pepperoni == "Y":
        bill += add_pepp_med_lg_cost
elif size == "L":
    bill += large_pizza_cost
    if add_pepperoni == "Y":
        bill += add_pepp_med_lg_cost
        
if extra_cheese == "Y":
    bill += add_extra_cheeese_cost

print(f"Your final bill is ${bill}.")

#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1