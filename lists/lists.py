
print('''Welcome to the game of the lists. You can add, update,
      remove existing lists using this lists''')

list = list()
list.append("Mandar")
list.append("Dharmadhikari")
list.append("Architect")
list.append(10)

print(list)

list2 = list.copy()
print(list2)
list2.clear()
print(list2)
print(f'count of list is {len(list)}')
print(f'count of number 10 in list is {list.count(10)} count of number 10 in list 2 is {list2.count(10)}')

print('UNderstanding shallow copy')

list_original = ["Mandar", "Dharmadhikari"]
list_shallow_copied = []
list_shallow_copied = list_original.copy()
for item in list_original:
    print(f'item: {item} and address: {id(item)} \n')

for item in list_shallow_copied:
    print(f'item: {item} and address: {id(item)} \n')


list_of_numbers1 = []
list_of_numbers2 = []

print(f"address of list_of_numbers1 is {id(list_of_numbers1)} and address of list_of_numbers2 is {id(list_of_numbers2)}")

for i in range(100, 110, 2):
    list_of_numbers1.append(i)

print(list_of_numbers1)

for i in range(110, 120, 2):
    list_of_numbers2.append(i)

print(list_of_numbers1 + list_of_numbers2)

list_of_numbers1.extend(list_of_numbers2)
print(list_of_numbers1)

i = 0
while i < len(list_of_numbers1):
    print(list_of_numbers1[i])
    i += 1
