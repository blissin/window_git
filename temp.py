A=[20,55,67,82,45,33,90,87,100,25]
a=0
for i in range(len(A)):
    if A[i]>=50:
        a+=A[i]
        print(a)
print(a)