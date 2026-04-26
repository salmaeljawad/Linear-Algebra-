import numpy as np

#  Scalars
a = 5
print("Scalar:", a)

#  Vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("\nVector v1:", v1)
print("Vector v2:", v2)

#  Matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

#  Shapes
print("\nShape of A:", A.shape)
print("Shape of v1:", v1.shape)

# Basic Operations

# +
print("\nA + B:\n", A + B)

# -
print("\nA - B:\n", A - B)

# * num
print("\n2 * A:\n", 2 * A)

# times
print("\nA @ B:\n", A @ B)

print("\nDot product v1.v2:", np.dot(v1, v2))

v = np.array([10, 20])
print("\nA + v:\n", A + v)