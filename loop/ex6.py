s = 0
maximum = 0
minimum = 100
amount = 0

while True:
    try:
        grade = eval(input("Enter a grade (press -1 if you wanna leave):  "))
        if grade == -1:
            break
        if not(0<=grade<=100):
            print("INVALID")
            continue
        
        amount +=1
        s += grade

        if grade > maximum:
            maximum = grade
        if grade < minimum:
            minimum = grade

    except:
        pass

print(f"Count: {amount}")
print(f"AVG: {s/amount}")

phrase = f"Worst grade is: {minimum}"
print(phrase)

phrase = "Best grade is: %s" %(maximum)
print(phrase)
    