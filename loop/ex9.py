counter = 0; su = 0; greater = 0

num = float(input("Insert a positive number: "))

while num > 0:
    su += num
    if greater < num:
        greater = num
    counter += 1
    num = float(input("Insert a positive number: "))

AVG = su/counter

print("\nNumbers inserted: %d" % (counter))
print("Sum: %d" % (su))
print("AVG: %.2f" % (AVG))
print("greater: %d" % (greater))