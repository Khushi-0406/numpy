import numpy as np
from datetime import datetime
import sys

a= np.array([10,20,30])
b=np.array([1,2,3])

print(type(a)) #<class 'numpy.ndarray'>

# traditional python code for numpy here
def dot_product(a,b):
    for m, n in zip(a, b):
        result =0
        result = result + (m*n)
    print("dot product:- ", result)
before = datetime.now()
dot_product(a,b)
after =datetime.now()
print("time:-" , after-before)

# using the numpy function
before = datetime.now()
np.dot(a,b)
after =datetime.now()
print("time:-" , after-before)

#vector functions of list and array
l=[10,20,30]
# l+2 -- error
a=np.array([10,20,30])
print(a+2)


# to check size of array and list
lst = [10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100]
ary = np.array([10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100])
print('The Size of list l => ',sys.getsizeof(lst)) #respect to the memeory
print('The Size of ndarray a => ',sys.getsizeof(ary))

"""
Python List Vs Numpy Array
Similarities:
1. Both can be used to store data
2. The order will be preserved in both. Hence indexing and slicing concepts are
applicable.
3. Both are mutable, ie we can change the content.
Differences:
1. list is python's inbuilt type. we have to install and import numpy explicitly.
2. List can contain heterogeneous elements. But array contains only homogeneous
elements.
3. On list, we cannot perform vector operations. But on ndarray we can perform vector
operations.
4. Arrays consume less memory than list.
5. Arrays are superfast when compared with list.
6. Numpy arrays are more convenient to use while performing complex mathematical
operations

"""