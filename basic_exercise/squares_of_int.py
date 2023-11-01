# Write a short python function which accepts a positive integer an and returns the sum
# of squares of all the odd positive integers less than n.
try:
    input_n = int(input("Enter a integer value.: "))
    i = 1
    sum = 0
    while i < input_n:
        print(f"{i} {input_n}")
        if (i & 1) != 0:
            sum += (i * i)
        i += 1
    print(f"Sum of odd integers less than {input_n} is {sum}")

except (ValueError, EOFError):
    print("Entry is not valid integer")