#tip calculator-#bill/num of people*1.12

print("Welcome to the tip calculator. ")
total_bill = float(input(f"What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

customers = int(input("How many people split the bill?"))

result = total_bill/customers * (tip/100+1)
new_result = round(result, 2)
print(f"Each person should pay: {new_result}")

