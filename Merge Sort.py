def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[p + i]

    for j in range(0, n2):
        R[j] = arr[q + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = p  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(A,p,r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


# Driver code to test aboves
A = [10, 7, 8, 9, 1, 5, 11, 2, 15, 4]
n = len(A)
merge_sort(A,0,n-1)
print ("Sorted array is:",A)

