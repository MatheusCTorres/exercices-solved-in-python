arr = []

for i in range(10):
    arr += input("Insert a word: ")

for word in arr:
    print(word)

word_a = [word for word in arr if word[-1] == "a"]

for word in word_a:
    print(word)

size_max = max(len(word) for word in arr)

for word in arr:
    if len(word) == size_max:
        print(word)
        break
