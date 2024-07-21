import numpy as np
import math

deg = 60

m = np.array([[math.cos(math.radians(deg)), -math.sin(math.radians(deg))], \
              [math.sin(math.radians(deg)),  math.cos(math.radians(deg))]])

v0 = [3, 0]
v1 = [5, 0]
v2 = [5, 2]
v3 = [3, 2]

print(np.matmul(m, v0))
print(np.matmul(m, v1))
print(np.matmul(m, v2))
print(np.matmul(m, v3))
