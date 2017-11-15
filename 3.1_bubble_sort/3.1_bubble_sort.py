from random import randint

N = int(input('Enter the count of list elements for sorting: '))

L = [randint(1, 100) for i in range(N)]

for i in range(N-1):
    for j in range(N-1-i):
        if L[j+1] < L[j]:
            L[j], L[j+1] = L[j+1], L[j]

print(L)