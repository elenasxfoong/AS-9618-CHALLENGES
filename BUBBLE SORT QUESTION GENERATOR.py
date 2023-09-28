import random
student_answer = []
numbers = []

length = int(input("how long do you want it to be:"))
for i in range(length):
  number = random.randint(0,99)
  numbers.insert(i,number)

print("solve:", numbers)

range = len(numbers)
boundary = range - 1
NoSwaps = True  
while NoSwaps == True: 
  NoSwaps = True
  for j in range (0,boundary): 
    for i in range(0,boundary):
      if numbers[i] > numbers[i+1]: 
        Temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = Temp
        NoSwaps = False 

first_answer = int(input("input the first number:"))
student_answer.append(first_answer)
for i in range(range - 1):
  next_answer = int(input("input the next number:"))
  student_answer.append(next_answer)

if student_answer == numbers:
  print("you got it right")
else:
  print("oh no you got it wrong, the correct answer is:", numbers)

  
