"""1.	Add two matrix and find the transpose of the resul"""


import numpy as np

def matrix_operations(mat_a, mat_b):
    try:
        array_a = np.array(mat_a)
        array_b = np.array(mat_b)
        
        if array_a.shape != array_b.shape:
            raise ValueError("Matrices must have identical dimensions")
        
        sum_matrix = array_a + array_b
        
        transposed_matrix = sum_matrix.T
        
        return sum_matrix, transposed_matrix
    except Exception as error:
        return str(error)


data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

sum_result, transposed_result = matrix_operations(data1, data2)
print("Matrix Sum:")
print(sum_result)
print("\nTransposed Sum:")
print(transposed_result)