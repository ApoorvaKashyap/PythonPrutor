import numpy as np
from scipy import linalg

try:
  a = np.array(eval(input()))
  b = np.array(eval(input()))
  x = linalg.solve(a,b)
except:
  print("ERROR: Cannot find solution.")
else:
  print(x)
