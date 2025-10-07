import numpy as np

# when we want to acess a single element then we go for indixing
# starts from zero indexing
#  a[i],   a[r][c],   a[b][r][c]

help(np.array)

"""
ndim :- eg 1-d, 2-d, 3-d
shape:- (4,),(2,3),(3,3)
size :- total element
dtype:- int 64, float32
itemsize :- size of array in byte
"""
import numpy as np

# Basic properties of arrays
a = np.array([10, 20, 30, 40])
print("1D array a:")
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print()

a = np.array([[10, 20, 30],
              [40, 50, 60]], dtype=float)
print("2D array a:")
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print()

# 1D array indexing example
a = np.array([10, 20, 30, 40, 50])
print("1D Array:", a)
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print("a[0] =", a[0])
print("a[2] =", a[2])
print("a[-1] =", a[-1])
print()

# 2D array indexing example
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("2D Array a:")
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print("a[0,0] =", a[0,0])
print("a[1,2] =", a[1,2])
print("a[2] =", a[2])
print()

# 3D array indexing example
c = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print("3D Array c:")
print("ndim:", c.ndim)
print("shape:", c.shape)
print("size:", c.size)
print("dtype:", c.dtype)
print("itemsize:", c.itemsize)
print("c[0,0,0] =", c[0,0,0])
print("c[1,1,2] =", c[1,1,2])
print("c[0,:,1] =", c[0,:,1])
print("c[:,1,0] =", c[:,1,0])
print("c[:,:,-1] =", c[:,:,-1])
