import numpy as np





# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(x):
    if x > 0:
        return 1
    else:
        return -1
#try with an example
#print(step(7))
#print(step(-5))


# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------

def ReLU(array, cutoff = 0):
    array = np.array(array)
    array[array < cutoff] = cutoff
    return array

test_array = np.array([])
print(ReLU(test_array,cutoff= 1))

#suggestion by chatgpt for efficient code
#def ReLu(arr, cutoff = 0):
    #return np.maximum(arr, cutoff)

#try thsi code:
#arr1 = [1, -2, 4, 5, -7]
#print(ReLu1(arr1)) #using default cutoff
#print(ReLu(arr1))

#using different cutoff value
#print(ReLu1(arr1, cutoff=-1)) #cutoff set to -1 here

# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

#two array - A and B for multiplication - A = 3X4 and B = 4X1
#A = np.array([1,2,3,4],
           #  [2,3,4,5],
            # [1,2,1,1])
#B = np.array([1,1,1,2])

def ReLu(array, cutoff = 0):
    array = np.array(array)
    array[array < cutoff] = cutoff
    return array

def neural_net_layer(A,B):
    result = A @ B #matrix multiplication
    return ReLu(result) #apply ReLu

#lets try
#print(neural_net_layer(A,B))


# ------------------------------------------