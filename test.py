def solution(A):
    j = 1
    while A:
        x = [A.pop(0) for num in range(j) if A]
        print("List:",x,"\tSum:",sum(x),"\tAverage:",sum(x)/len(x))
        j += 1



A = [i for i in range(1,18)]
solution(A)

