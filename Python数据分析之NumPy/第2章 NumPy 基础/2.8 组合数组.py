import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

b = 2 * a
print(b)

# 水平组合a和b,两种方式
print( np.hstack((a,b)) )

print( np.concatenate((a,b), axis=1) )

# 垂直组合a和b,两种方式
print( np.vstack((a,b)) )

print( np.concatenate((a,b), axis=0) )

# 深度组合a和b
print( np.dstack((a,b)) )

# 列组合a和
oned = np.arange(2)
print(oned)
twice_oned = 2 * oned
print(twice_oned)
print( np.column_stack((oned,twice_oned)) )

print( np.column_stack((a,b)) )

# column_stack函数和hstack函数效果相同
print( np.column_stack((a,b)) == np.hstack((a,b)) )

# 行组合a和b
print( np.row_stack((oned,twice_oned)) )

print( np.row_stack((a,b)) )

# row_stackh函数和vstack函数效果相同
print( np.row_stack((a,b)) == np.vstack((a,b)) )