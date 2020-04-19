while True:
    try:
        num = int(input("Enter a number between 1000 and 10000: "))
        if (1000 <= num <= 10000):
            break
    except:
        print("TRY AGAIN")
        pass

for n in range(1, num+1):
    for i in range(2, n//2+1):
        if n%i==0:
            break
    else:
        print(n, end=" ")