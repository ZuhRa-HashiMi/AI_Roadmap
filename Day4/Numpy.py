import numpy as np

v1 = np.array([2, 3])
v2 = np.array([-1, 4])

print("v1:", v1)
print("v2:", v2)

print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)
print("v1 * 3:", v1 * 3)

dot_product = np.dot(v1, v2)
print("dot product:", dot_product)

norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)

print("norm of v1:", norm_v1)
print("norm of v2:", norm_v2)

cosine_similarity = dot_product / (norm_v1 * norm_v2)

print("cosine similarity:", cosine_similarity)