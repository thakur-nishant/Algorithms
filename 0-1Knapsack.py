def knapSack(total_weight, item_weight, item_value):
    n = len(item_value)
    K = [[0 for x in range(total_weight + 1)] for x in range(n + 1)]
    # print(K)
    # K = [[0] * (total_weight + 1)] * (n + 1)
    # print(K)
    for i in range(n + 1):
        for w in range(total_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif item_weight[i - 1] <= w:
                K[i][w] = max(item_value[i - 1] + K[i - 1][w - item_weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    print(K)
    return K[n][total_weight]


def knap_sack_dp(W, wt, val):

    K = [[0 for j in range(W+1)] for i in range(len(wt))]
    # we don't need the boundary condition to check if its the first row because,
    # in python -1 points to the last index of the list and as we have all list initialized to 0
    # we don't have a need to add an extra row with zeros at the top
    # this is not recommended though. its just to be over smart with logic. not necessary
    for i in range(len(wt)):
        for j in range(W+1):
            if i == 0 and j == 0:
                continue
            elif j < wt[i]:
                K[i][j] = K[i-1][j]
            else:
                K[i][j] = max(val[i]+K[i-1][j-wt[i]], K[i-1][j])
    # print(K)
    return K[len(wt)-1][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapSack(W, wt, val))


val = [1,4,5,7]
wt = [1,3,4,5]
W = 7
print(knap_sack_dp(W, wt, val))
