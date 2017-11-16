def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-1):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]


A = [12, 1, 5, 6, 15, 10, 6]
print(A)
bubble_sort(A)
print(A)