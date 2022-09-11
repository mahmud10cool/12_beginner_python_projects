A = [1,3,4,2,6,5,8,9,7]

for i in range(len(A)):
    key = A[i]
    j = i - 1
    while j > 0 and A[j] > key:
        A[j+1] = A[j]
        j = j - 1
    A[j + 1] = key
    print(f'Iteration number {i}: {A}\n')

print(f'Final solution: {A}')