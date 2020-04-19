grade = int(input("Insert a grade: "))

if grade < 4:
    print("Terrible")
elif 4 <= grade < 10:
    print("Too bad")
elif 10 <= grade < 14:
    print("Enought")
elif 14 <= grade < 17:
    print("Good")
else:
    print("Great")