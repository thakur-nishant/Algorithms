def solution(A):
    Sum = []
    Avg = []
    j = 1
    newA = []
    while A:
        x = []
        for num in range(j):
            if A:
                x.append(A.pop(0))

        newA.append(x)
        j += 1

    for i in newA:
        Sum.append(sum(i))
        Avg.append(sum(i)/len(i))

    print(Sum)
    print(Avg)


A = [i for i in range(1,18)]
solution(A)

