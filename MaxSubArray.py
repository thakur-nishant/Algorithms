def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -999999
    total_sum = 0
    max_left = low
    for i in range(low, mid):
        total_sum = total_sum + A[i]
        # print( total_sum, A[i])
        if total_sum > left_sum:
            left_sum = total_sum
            max_left = i
    right_sum = -999999
    total_sum = 0
    max_right = max_left
    for j in range(mid, high+1):
        total_sum = total_sum + A[j]
        # print(total_sum, A[j])
        if total_sum > right_sum:
            right_sum = total_sum
            max_right = j

    return [max_left, max_right, left_sum + right_sum]


def find_max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid +1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            print('left')
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            print('right')
            return [right_low, right_high, right_sum]
        else:
            print('cross')
            return [cross_low, cross_high, cross_sum]


A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
result = find_max_subarray(A, 0, len(A)-1)
print(result)
