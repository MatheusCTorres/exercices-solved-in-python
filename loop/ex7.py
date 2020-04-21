password = 1234

for attepmt in range(3, 0, -1):
    password_inserted = int(input("Insert your password (%d attempt): " % (attepmt)))

    if password_inserted == password:
        print("CORRECT PASSWORD")
        break
    print("WRONG PASSWORD")
else:
    print("YOU MISS YOUR 3 ATTEMPTS")