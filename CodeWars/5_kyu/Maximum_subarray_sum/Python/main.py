
def max_sequence(arr):
    if not arr or max(arr) < 0:
        return 0
    max_sum = 0
    cur_sum = 0
    for num in arr:
        cur_sum += num
        if cur_sum > max_sum:
            max_sum = cur_sum
        elif cur_sum < 0:
            cur_sum = 0
    return max_sum
