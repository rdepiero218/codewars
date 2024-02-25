#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:47:54 2024

@author: reggiemba
"""

import time
import numpy as np

start_time = time.time()


def smaller(arr):
    nums = np.array(arr)
    counts = []
    for i in range(len(nums)):
        count = 0
        val = nums[i]
        for j in range(i, len(nums)-1):
            if val > nums[j+1]:
                count += 1
        counts.append(count)
        
    return counts

## too slow
# def smaller(arr):
#     # print(arr)
#     counts = []
#     for i in range(len(arr)):
#         count = 0
#         sub = arr[(i+1)::]
#         for j in range(len(sub)-1):
#             if int(arr[i]) > int(sub[j]):
#                 count += 1
#         counts.append(count)
        
#     return counts


# using list comprehension
# def smaller(arr):

#     counts = [sum(arr[i] > arr[j+1] for j in range(i, len(arr)-1)) for i in range(len(arr))]
        
#     return counts

# original easier and slow for 1 million
# def smaller(arr):
#     counts = []
#     for i in range(len(arr)):
#         count = 0
#         for j in range(i, len(arr)-1):
#             if arr[i] > arr[j+1]:
#                 count += 1
#         counts.append(count)
    
#     return counts



numbers = list(range(1_000_000))
numbers.reverse()
# print(numbers)
smaller(numbers)

# print(sum(numbers))

print("--- %s seconds ---" % (time.time() - start_time))