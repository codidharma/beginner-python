numbers = [1,2,3,6,7]

# While loop

loopCounter = 0

while loopCounter < len(numbers):
    print(numbers[loopCounter])
    loopCounter += 1

# For

for number in numbers:
    print(number)

# For with enumerator

for index, number in enumerate(numbers):
    print(f"{index} and {number}")

# Zip Function
chars1 = ['a', 'b', 'c', 'd']
chars2 = ['z', 'y', 'x', 'w', 'v']

index = 0
while index < len(chars1) and len(chars2):
    print(chars1[index], chars2[index])
    index += 1


# Same with zip code
for index1, index2 in zip(chars1, chars2):
    print(index1, index2)


# The exception is still thrown when the loop completes execution
# for char in chars1:
#     print(char)

# else:
#     raise Exception("Some exception")

exception_required = False
# break escapes the else
for char in chars2:
    if char == 'y':
        exception_required = True
        break

if exception_required:
    raise Exception("Some exception")