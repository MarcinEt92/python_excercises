import math


def switch_bit(number: str, which_bit):
    bit_index = len(number) - 1 - which_bit
    bit_value = int(number[bit_index])

    number = int(number, 2)

    if bit_value == 1:
        number = number - math.pow(2, which_bit)
    else:
        number = number + math.pow(2, which_bit)
    return bin(int(number))


print(switch_bit("0b101000101", 3))
