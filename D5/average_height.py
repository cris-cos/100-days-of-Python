student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
average = 0.0
for i in range(0, len(student_heights)):
    total += student_heights[i]
    average = total / (i + 1)

print(average)