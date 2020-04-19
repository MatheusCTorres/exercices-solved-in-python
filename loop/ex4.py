while True:
    try:
        num = int(input("Enter a number: "))
        if 0<=num:
            break
    except:
        print("Enter again")
        pass

for i in range(2, num):
    if num%i==0:
        print("{} is not prime".format(num))
        break
else:
    print("{} is prime".format(num))