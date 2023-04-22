#fruits = ["Apple", "Peach", "Pear"] 
#for x in fruits:
#    print(x)
#    print(x + " pie")



#while loops---only put true or false statements
#number_of_loops = 4
#while number_of_loops > 0:
  #  print("it's time to party") 
 #   number_of_loops -= 1  

#print(5)
#x = 5
#print(x + 1)

word = "laampy"
guess = input("Guess a letter! a")
display = ["_", "_", "_", "_", "_"]
word_length = len(word)
for position in range(word_length):
    letter = word[position]
    if guess == letter:
        display[position] = letter
print(display)