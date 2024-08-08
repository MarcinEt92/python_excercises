"""
Napisz program który zamieni na przeciwny jeden bit z ciągu
"""



def change_bit(num: int, bit: int):
    bit_value = num & 1 << bit
    print(bit_value)



def answer():
    sequence = 0b11001
    which_bit = 3

    print(sequence)

    change_bit(sequence, which_bit)

if __name__ == "__main__":
    answer()

    

