import random
import numpy as np

a = input("Enter ID: ")
number = int(a[-2:])
# print(a[6:8])
# b=93
print("number = %d" % number)
num1 = randnums= np.random.randint(10,99,1000)
num1.sort() 
print("Random integer: ", num1)
count = 0
for i in range(1, 1001):
    if num1[i] == number:
      count = count+1
    if num1[i] > number:
      break  
print("count = %d" % count)
if count > 3:
    print("GET A")
else :
    print("GET F")