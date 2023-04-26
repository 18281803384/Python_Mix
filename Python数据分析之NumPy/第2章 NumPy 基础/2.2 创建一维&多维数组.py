import numpy as np

print("-----一维数组-----")
a = np.arange(5)
print(a)
print(a.shape)
print(a.dtype)

print("-----多维数组-----")
b = np.array([np.arange(2), np.arange(2)])
print(b)
print(b.shape)
print(b.dtype)

print("-----选取数组元素-----")
c = np.array([[1,2],[3,4]])
print(c)
print(c[0,0], c[0,1])
print(c[1,0], c[1,1])
