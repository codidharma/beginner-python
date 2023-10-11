# Write a short python function , is_even(k) that takes an integer value and returns true if k is even
# and false otherwise. Your function can not use the multiplication, modulo or division operators

def is_even(k:int):
    is_k_even = False
    if (k & 1) == 0:
        is_k_even = True

    return is_k_even


k = int(input('Enter an integer value for k'))
print(is_even(k))