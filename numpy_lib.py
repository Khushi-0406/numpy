import numpy as np

# difference between list and array
lst=[1,2,3,4]
lst_result =[x+2 for x in lst]
print(lst_result)

arr = np.array([1,2,3,4,5,6,7,8,9])
arr_result = arr+ 2
print(arr_result)

# multidimensional array
a=np.array([1,2,3])
print("1D-array:-\n ",a)

b=np.array([[1,2,3],[4,5,6]])
print("2D-array:-\n ",b)

c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("3D-array:- \n",c)

# array slicing operator
arr=np.array([10,20,30,40,50])
print(arr[1:4])
print(arr[-3:])

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix[:2,1:]) #matrix[row_start:row_end , col_start:col_end]

# operations of array
arr= np.array([1,2,3,4])

print("add 5:- " , arr+5)
print("multiply by 2 :- " ,arr*2)
print('square:- ', arr**2)
print("subract:- ", arr-2)
print("sin:- ", np.sin(arr))

# functions of array
arr= np.array([10,20,30,40,50])
print("Mean:-", np.mean(arr))
print("median:-", np.median(arr))
print("standard deviation:-", np.std(arr))
print("sum:- ", np.sum(arr))

# reshaped and flatten
arr= np.arange(1,13)
print("Original:-\n", arr)

reshaped = arr.reshape(3,4)
print("reshaped:-\n", reshaped)

flattened= reshaped.flatten() #convert multi-dimensional array to one-dimensional array
print("flattened:-\n", flattened)

# matrix multiplication
a=np.array([[1,2],[3,4]])
b=np.array([[4,5],[6,7]])
print("matrix multiplication:- ", np.dot(a,b))

# random array
rand_arr = np.random.randint(1,10, size=(3,3))
print("random matrix:-\n", rand_arr)

arr2D = np.array([[1,2,3],[4,5,6]])
arr1D = np.array([10,20,30])
print("broadcasted:-", arr1D+arr2D)