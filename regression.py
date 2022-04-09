#regression : input 들어온걸로 
import numpy as np
import pandas as pd

# X=[]
# X=np.array(X)
# X=np.full(20,1)
# print(X)
# print(type(X))
a=[]
X=[]
for i in range(5):
    X=[]
    for j in range(20):
        X.append(j+1)
        # print("X : ",X)
    a.append(X)
    # print("a : ",a)

a=np.array(a)
print(a)
print(a.shape)
print(type(a))

a=np.delete(a,12,axis=1)
print(a)
print(a.shape)

# a=pd.DataFrame(a)
# print(a)
# print(a.shape)
# print(type(a))

# print(a[0][1])

