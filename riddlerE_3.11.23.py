import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def get_2digits(number): #get two last digits out of number
    first = get_digit(number, 0)
    if len(str(number)) == 1:
        return first
    second = get_digit(number, 1)
    return second*10+first

def get_digit(number, n): # get n digit out of number
    return number // 10**n % 10

numbers = 500000
summe = 0
end_digits = list()

for i in range(1,numbers):
    summe += i
    #print(i, summe)
    digits = get_2digits(summe)
    #print(digits)
    end_digits.append(digits)

df = pd.DataFrame (end_digits, columns = ['end digits'])
data = df.value_counts(normalize=True).sort_values().sort_index()

print(data)

#most common last digits
# 03 / 28 / 53 / 78