while True:
    try:
        num = int(input("Enter a number: "))
        if 0<=num:
            break
    except:
        print("Enter again")
        pass

for i in range(0,num):
    if i % 3 == 0 and i%5!=0:
        print(i, end=" ")