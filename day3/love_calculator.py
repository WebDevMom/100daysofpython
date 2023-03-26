print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

true_score = 0
love_score = 0

true_score += name1.count("t")
true_score += name1.count("r")
true_score += name1.count("u")
true_score += name1.count("e")

love_score += name1.count("l")
love_score += name1.count("o")
love_score += name1.count("v")
love_score += name1.count("e")


true_score += name2.count("t")
true_score += name2.count("r")
true_score += name2.count("u")
true_score += name2.count("e")

love_score += name2.count("l")
love_score += name2.count("o")
love_score += name2.count("v")
love_score += name2.count("e")

final_love_score = int(str(true_score) + str(love_score))

if final_love_score < 10 or final_love_score > 90:
    print(f"Your score is {final_love_score}, you go together like coke and mentos.")

elif final_love_score >= 40 and final_love_score <= 50:
    print(f"Your score is {final_love_score}, you are alright together.")

else:
   print(f"Your score is {final_love_score}.")


