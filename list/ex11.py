writers = [['Pedro', 'Tamen Garret'], 
              ['Almeida', 'Garrett' ], 
              ['Camilo', 'Pessanha'], 
              ['Almada', 'Negreiros'], 
              ['Ibn', 'Bassam'], 
              ['Antonio', 'Aleixo Silva Zebedeu'], 
              ['Ricardo', 'Reis'],
              ['Mario', 'Sá-Carneiro'], 
              ['Mario', 'Cesariny Ana'], 
              ['Luis', 'Camões'], 
              ['Miguel', 'Torga'], 
              ['Natália', 'Correia'], 
              ['Tolentino', 'Mendonça']] 

list_name = [len(name) for name, surname in writers]
size_list_of_name = max(list_name)

size_list_of_surname = max(len(surname) for name, surname in writers)

writers.sort(key = lambda arr: arr[1].split()[-1])

for name, surname in writers:
    print("%-*s %-*s" % (size_list_of_name, name, size_list_of_surname, surname))