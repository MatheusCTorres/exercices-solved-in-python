while True:
    try:
        num = int(input("Enter a number: "))
        if 1<=num<=10:
            break
    except:
        print("ENTER AGAIN")
        pass

for i in range(0,11):
    print(f"{i:2} x {num} = {i*num:3}")