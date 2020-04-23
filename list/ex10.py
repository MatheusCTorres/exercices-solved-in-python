from math import sqrt

grades = [15, 20, 18, 17, 4, 16, 3, 4, 18, 14, 3, 0, 14, 2, 20, 17, 15, 3, 15, 4, 15, 1]

positive=[]
negative=[]

for grade in grades:
    if grade < 10:
        negative += [grade]
    else:
        positive += [grade]

print("positive grades: ", positive)
print("negative grades: ", negative)

neg_grade = pos_grade = negative[0]

adding = 0

for grade in negative:
    if grade < neg_grade:
        neg_grade = grade

    if grade > pos_grade:
        pos_grade = grade

    adding += grade

avg = adding/len(negative)

adding = 0
for grade in negative:
    adding += (grade-avg)**2

standard_deviation = sqrt(adding/len(negative))

print("max: {}".format(pos_grade))
print("min: {}".format(neg_grade))
print("avg: {:.2f}".format(avg))
print("standard deviation: {:.2f}".format(standard_deviation))