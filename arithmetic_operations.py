# +  -  *  /  //  **  %

# difference between division(/) and flore division(//)
print(4/2)
print(4//2)
print(4.0//2)

print(3/2)
print(3//2)
print(3.0//2)

# arithmetic operations on the 1-D array
print(10+2)
print(10-2)
print(10*2)
print(10/2)
print(10//2)
print(10%2)
print(10**2)

# for numpy arrays with scalar(constant numeric value):

import numpy as np

a=np.array([10,20,30,40,50])
print(a+2)
print(a*2)
print(a-2)
print(a//2)
print(a/2)
print(a%2)
print(a**2)
print(a/0) #[inf inf inf inf inf]

# Arithmetic operations on the 2-D array

l=[[10,20,30],
    [40,50,60]]
a=np.array(l)
print(a.ndim)
print(a+2)
print(a*2)
print(a-2)
print(a//2)
print(a/2)
print(a%2)
print(a**2)

# arithmetical operation array to array
a=np.array([100,200,300,400])
b=np.array([10,20,30,40])
print(a+b)
print(a*b)
print(a-b)
print(a//b)
print(a/b)
print(a%b)
print(a**b)


