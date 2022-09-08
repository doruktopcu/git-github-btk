import numpy as np
import random as rand

a_new_array = np.zeros((8,8))

for i in range(8):
    for j in range(8):
        for k in range(rand.randint(10,200)):
            a_new_array[i,j] = k

print(a_new_array)