def knap_sack(W, wt, val, n):
    val_per_wt = [0] * n
    sack_weight = []
    sack_value = []
    for i in range(n):
        val_per_wt[i] = val[i]/wt[i]

    while W > 0 and len(val_per_wt) != 0:
        x = val_per_wt.index(max(val_per_wt))
        del val_per_wt[x]
        sack_value.append(val[x])
        sack_weight.append(wt[x])
        W -= wt[x]
    print(sack_value)
    print(sum(sack_value))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
knap_sack(W , wt , val , n)
