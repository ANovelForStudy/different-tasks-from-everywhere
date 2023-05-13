

def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            for j in range(i+1, len(lst)):
                if lst[j] != 0:
                    lst[i], lst[j] = lst[j], lst[i]
                    break

    return lst
