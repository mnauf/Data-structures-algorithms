print("Anum is a bad girl");
import numpy as np
import time
t1=time.time()
A=np.array([
[1,2,3],
[4,5,6]
])
B=np.array([
[1,2,3],
[4,5,6]
])
print(A+B)
t2=time.time()
print("The program took ", t2-t1," seconds");
 
