fruits = ["Apple", "Banana", "Peach"]

for fruit in fruits:
    print(fruit)

'''
Consider downloading the Thonny IDE: https://thonny.org/
'''
#student_heights = input().split()
student_heights = "156 178 165 171 187".split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  

print(student_heights)

students_total = len(student_heights)
heights_total = 0
for height in student_heights:
   heights_total += height

#print(f"There are a total of {students_total} heights in student_heights")

avarage_height = round(heights_total/students_total)

#print(f"Average height rounded to the nearest whole number = {avarage_height}")

print(f"total height = {heights_total}")
print(f"number of students = {students_total}")
print(f"average height = {avarage_height}")

print("\n\nREPLICATING THE PYTHON MAX FUNCTION")
#student_scores = input().split()
student_scores = "78 65 89 86 55 91 64 89".split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = student_scores[0] 
scores_total = len(student_scores)
for n in range(0, scores_total):
   if student_scores[n] > max_score:
      max_score = student_scores[n]

print(f"The highest score in the class is: {max_score}")

print("\n\nADDING EVEN NUMBERS")

#target = int(input())
target = 10
target = 52


def add_even(target):
   numbers = []
   even_numbers = []
   sum = 0
   start = 1

   while start <= target:
      numbers.append(start)
      if start % 2 == 0:
         sum += start
         even_numbers.append(start)
      start +=1
   print(sum)
   #print(f"These are all the numbers: {numbers}\nThese are all the even numbers that were added: {even_numbers}")

add_even(target)

even_sum = 0
for number in range(2, target + 1, 2):
   even_sum += number
print(even_sum)

print("\n\nTHE FIZZBUZZGAME")

for number in range(1, 101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
     print("Buzz")
  elif number % 3 == 0:
     print("Fizz")
  else:
     print(number)
