import numpy as np
import random as rand

a_new_array = np.zeros((8,8))

for i in range(8):
    for j in range(8):
        for k in range(rand.randint(10,200)):
            a_new_array[i,j] = k

print(a_new_array)

#We created a random matrix, good job!

def a_new_function(takes_integer, modulo_integer):
    finds_the_remainder = takes_integer % modulo_integer
    possible_numbers_list = list()

    for k in range(73):
        finds_the_possible_number = finds_the_remainder + k * modulo_integer
        possible_numbers_list.append(finds_the_possible_number)

    return possible_numbers_list

we_asked_for_it = a_new_function(100,3)
print(we_asked_for_it)

#Congratz, now you have a list of numbers which has the same remainder, according to the number and the modulu you have entered.