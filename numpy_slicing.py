# when we want access multipal elements then we go for slicing
# slicing a part of an array

# a[begin:end:step]
# a[begin:end:step,begin:end:step]
# a[begin:end:step,begin:end:step,begin:end:step]

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a[2:6])
print(a[2:])
print(a[:5])
print(a[::-1])
print(a[::2])
print(a[::3])
print(a[5:1:-1])

# 2-D array
a=np.array([[10,20],[30,40],[50,60]])

'''
        -2  -1
         0   1
-3  0   |10|20|
-2  1   |30|40|
-1  2   |50|60|

'''

print(a.shape, a.size, a)
# a[row,cloumn]  a[begin:end:step, begin:end:step]
print(a[:,0:1])
print(a[1:2,:]) #first row all columns
print(a[0:2,:]) #two rows two columns
print(a[::2,:])

# slicing on 2-D array
a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Shape:", a.shape)
print("Size:", a.size)
print("Dimensions:", a.ndim)
print("array:-", a)
# a[row,cloumn]  a[begin:end:step, begin:end:step]
print(a[::3,:])
print(a[:,::2])
print(a[1:3,1:3])
print(a[1:3,::3])
print(a[::3, ::3])

#slicing on 3-D array
l= [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
a=np.array(l)
print("array:-", a)
print("Shape:", a.shape)
print("Size:", a.size)
print("Dimensions:", a.ndim)
# a[block:rows:cloumns]
print(a[:,:,:1])
print(a[:,2:,:])
print(a[:,:2,1:3])
print(a[0:1,:1,:]) #first block
print(a[0,0,:])