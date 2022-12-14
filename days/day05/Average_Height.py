student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

totalHeights = numberOfHeights = averageHeight = 0
for i in student_heights:
    numberOfHeights += 1
for i in range(0, numberOfHeights):
    totalHeights += student_heights[i]
averageHeight = round(totalHeights / numberOfHeights)
print(averageHeight)
