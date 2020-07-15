#Problem 2
#Given an array of integers, return a new array such that each element at index i of the new array is the 
#product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6]
import numpy as np
import time

def product_all(num):
    return [int(np.prod(num)/i) for i in num]

print(product_all([1, 2, 3, 4, 5]))

#Follow up: What if we can't use division
def product_without_div(num):
    return_num = []
    for i in num:
        num.remove(i)
        return_num.append(int(np.prod(num)))
        num.append(i)
    return return_num

product_without_div([1, 2, 3, 4, 5])