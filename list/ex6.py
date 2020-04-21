arr_grade = [0]*4+[20]*4

sumation = 0; n_grade = 0

for grade in arr_grade:
    sumation += grade
    n_grade +=1
avg = sumation / n_grade

sum_deviation =0
for grade in arr_grade:
    sum_deviation += (grade-avg)**2
deviation = (sum_deviation / n_grade)**(1/2)

print(arr_grade)
print("AVG: ", avg)
print("Standard deviation: ", deviation)