student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

 #create a for loop that adds up all the student heights 
total = 0
count = 0
for height in student_heights:
  total += height
  count += 1
average = round(total/count)
  
print(average)