import time
X = [6,3,5,1,3,2,9,2,1,8]*10
print(X)

#logic implemented by me
def insertion_sort():
    for i in range(1,len(X)):
        key = i
        j = i - 1
        while j >= 0:
            if X[key]<X[j]:
                X[key], X[j] = X[j], X[key]
                key = j
            j = j -1

#logic from CLRS
def insertion_sort_clrs():
    for i in range(1,len(X)):
        key = X[i]
        j = i-1
        while j>=0 and X[j] > key:
            X[j+1] = X[j]
            j = j - 1
        X[j+1] = key

t1 = time.time()
#call function
insertion_sort()
t = time.time() - t1
print(t)

#resetting the array X
X = [6,3,5,1,3,2,9,2,1,8]*10

t2 = time.time()
#call function
insertion_sort_clrs()
t = time.time() - t2
print(t)
#print the sorted array
print(X)
