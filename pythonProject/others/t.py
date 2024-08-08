import json
import re
from datetime import datetime, timedelta
import itertools
import math
import string

# Create a list with values ranging from 0 to 9.

my_list = list(range(0, 10))
print(my_list)

# Convert a list of integers to a list of strings.

my_list_str = [str(elem) for elem in my_list]
print(my_list_str)

# Multiply all elements in a list by 2.

pow_list = list(map(lambda x: x * x, my_list))
print(pow_list)

# Extract all odd numbers from a list of integers.

odd_nums = [elem for elem in my_list if elem % 2 != 0]
print(odd_nums)

# Replace all odd numbers in a list with -1.

negative_one_list = []
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        negative_one_list.append(my_list[i])
    else:
        negative_one_list.append(-1)
print(negative_one_list)

# Convert a list of integers to a list of booleans where all non-zero values become True.

lst = [-1, 2, 0, -4, 5]

bool_list = [bool(elem) for elem in lst]
print(bool_list)

# Replace all even numbers in a list with their negative.

even_neg_list = []
for elem in my_list:
    if elem % 2 == 0:
        even_neg_list.append(-1 * elem)
    else:
        even_neg_list.append(elem)

print(even_neg_list)

# sort (ascending and descending) a dictionary by value

my_dict = {
    "name": "Mark",
    "surname": "Kowalski",
    "country": "Poland",
    "city": "Gdansk"
}
my_dict["district"] = "Oliwa"
d_sorted = sorted(my_dict.items(), key=lambda d: d[1], reverse=True)
print(dict(d_sorted))

# Wconcatenate the following dictionaries to create a new one

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d4 = dict()

list_of_d = [dic1, dic2, dic3]
for d in list_of_d:
    d4.update(d)
print(d4)

# Check If key is preset

if "a" in my_dict.keys():
    print("key exists")
else:
    print("key does not exist")

# Write a Python program to iterate over dictionaries using for loops

for k, v in my_dict.items():
    print(f"{k} => {v}")

d = sorted(my_dict.items(), key=lambda d: d[1])
print(d)

# generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

pow_d = dict()

for i in range(1, 6):
    pow_d[i] = i * i
print(pow_d)

# program to remove a key from a dictionary

my_dict.pop("district")
print(my_dict)

# Write a Python program that iterates over elements as many times as its count.
col = ['p', 'p', 'p', 'p', 'q', 'q']
col_iter = itertools.cycle(col)
for _ in range(12):
    print(next(col_iter), end=" ")

print("/n")

# find most common letters in lkseropewdssafsdfafkpwe
my_str = "lkseropewdssafsdfafkpwe"
d_counter = dict()

for letter in my_str:
    if letter in d_counter.keys():
        d_counter[letter] += 1
    else:
        d_counter[letter] = 1

print(d_counter)
d_counter = (sorted(d_counter.items(), key=lambda x: x[1], reverse=True))
print(d_counter[0])

# str operations and lists operations
print("\nstr operations and lists operations\n")
my_str = "My sentence with apple, apple and apple"
print(my_str.replace("e", "a"))

template = str.maketrans("abcd", "efgh")
print("an apple".translate(template))
print(my_str.count("apple"))
if my_str.endswith("apple"):
    print("apple ended")

print(my_str.find("apple"))

# bit operations
print("\nbit operations")
a = 15
print("{0:b}".format(a))

# read bit
which_bit = 2
bit_val = int(bin(a)[len(bin(a)) - 1 - which_bit])

if bit_val == 1:
    a -= math.pow(2, which_bit)
else:
    a += math.pow(2, which_bit)

print("{0:b}".format(int(a)))

# eratos
max_range = 100
my_list = list(range(1, max_range))

for i in range(2, max_range // 2):
    for j in range(2 * i, max_range, i):
        if j in my_list:
            my_list.remove(j)

print(my_list)

# date time

t = datetime.now()
print(t.month)

d1 = datetime(2014, 5, 21)
d2 = datetime(2013, 4, 20)

print(d1 - d2)

d3 = d1 + timedelta(days=22)

print("\nITER\n")


class SomeInts:
    def __init__(self, max_r):
        self.max_r = max_r

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n > self.max_r:
            raise StopIteration
        self.n += 2
        return self.n


my_it = iter(SomeInts(20))

for i in my_it:
    print(i)

# str

my_str = " Rain in ,  Spain, but I feel, good"

print(my_str)
a = my_str.index(",")
b = my_str.find(",")
print(a)
print(b)

my_str_list = [element.strip() for element in my_str.split(",")]
print(my_str_list)

print(",".join(my_str_list))

# re

txt = "The rain in Spain and rain is ok"
found = re.findall("is ok$", txt)
print(found)

# JSON

with open("data.json", "r") as f:
    data_d = json.load(f)

print(data_d["glossary"]["GlossDiv"]["title"])


grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

grades_filtered = filter(lambda x: x[1] > 8, grades.items())

print(dict(grades_filtered))



