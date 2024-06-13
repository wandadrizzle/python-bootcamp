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