try:
    age = int(input("Insert an age: "))
    if age <= 0:
        print("Invalid age")
    elif age < 13:
        print("Kid")
    elif age < 18:
        print("Teenager")
    else:
        print("Adult")
except:
    print("Enter an integer number")