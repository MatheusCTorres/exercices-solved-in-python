try:
    num = int(input("Insert a number"))
    if num % 2:
        print(num, "is odd")
    else:
        print(num, "is even")
except:
    print("Insert an integer number")