import numpy as np

a= np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(b)

array= np.array([1,2,3,4,5])
print(array)
print(type(array))

l=[]
for i in range(5):
    int_1 = int(input("enter:-"))
    l.append(int_1)
print(np.array(l))

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.ndim)

arry3 = np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]])
print(arry3)
print(arry3.ndim)

# using buildin function

#array filled with zeros
ar_zero = np.zeros(4)
ar_zero2 = np.zeros((3,4))
print(ar_zero)
print(ar_zero2)

# array filled with ones
ar_one = np.ones(4)
ar_one2 = np.ones((3,4))
print(ar_one)
print(ar_one2)

# empty array
ar_em= np.empty(4)
print(ar_em)

# range array
ar_rn = np.arange(4)
print(ar_rn)

# identity array (diagnal same)
ar_dia = np.eye(4)
print(ar_dia)

# array filled with a fixed value
ar_full= np.full((2, 2), 5)
print(ar_full)

#line space
ar_ln = np.linspace(0,1,5)
print(ar_ln)


# using copy and view
a = np.array([1, 2, 3])
b = a.view()
c = a.copy()

a[0] = 100
print(a)
print(b)
print(c)
