password = "secret"
insert_password = input("Insert you password: ")

while insert_password != password:
    print("WRONG PASSWORD")
    insert_password = input("TRY AGAIN: ")
print("CORRECT PASSWORD")