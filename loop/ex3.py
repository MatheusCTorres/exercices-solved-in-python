while True:
    try:
        num = int(input("Enter a number: "))
        if 0<=num:
            break
    except:
        print("Enter again")
        pass

if num == 0:
    print (0)
elif num == 1:
    print(0, 1)
else:
    penultimate = 0
    last = 1
    print(0, 1, end=" ")

    for count in range(3, num+1):
        last, penultimate = last + penultimate, last
        print(last, end=" ")