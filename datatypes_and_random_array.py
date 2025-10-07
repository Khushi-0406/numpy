#datatypes in numpy arrays
import numpy as np

var = np.array([1,2,3,4,5])
print("data type:-", var.dtype)

var = np.array([1.0,2.4,3.3,4.6,5.2])
print("data type:-", var.dtype)

var = np.array([1,2,3,"A","H","O"])
print("data type:-", var.dtype)

x=np.array([1,2,3,4,5], dtype = float)
print("data type:-", x.dtype)

# array with random numbers
var= np.random.rand(4)
print(var)
var2 = np.random.rand(2,5)
print(var2)

var3= np.random.randn(5)
print(var3)

var4= np.random.ranf(5)
print(var4)

var5 = np.random.randint(0,10,3)
print(var5)