def max_heapify(A, n, i):
    large = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n and A[l] > A[i]:
        large = l
    if r < n and A[r] > A[i]:
        large = r
    if large != i:
        A[i], A[large] = A[large], A[i]
        max_heapify(A, n, large)


def build_max_heap(A):
    n = len(A)
    for i in range(0, n//2):
        max_heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    heap_size = n
    build_max_heap(A)
    for i in range(n-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        max_heapify(A, heap_size, 0)


A = [12, 11, 13, 5, 6, 7]
print(A)
heap_sort(A)
print(A)
