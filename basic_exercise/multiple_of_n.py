def is_multiple(n,m):
    return_value = False
    if n % m == 0:
        return_value = True

    return return_value

print('This program checks if n is a multiple of m, where n and m are both integers')
n = int(input('Enter the value of integer n'))
m = int(input('Enter the value of integer m'))

print(is_multiple(n,m))

