#You are going to write a program that calculates the sum of all the even numbers 
#from 1 to 100. Thus, the first even number would be 2 and the last one is 100:1 
#print statement in your console output. It should just print the final total and
#you will need to use the range() function in any of the solutions.

total = 0
for even_number in range(2, 101, 2):
    total += even_number
print(total)
