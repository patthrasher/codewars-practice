def sum_mix(arr) :
    # total = 0
    # for each in arr :
    #     total = total + int(each)
    # return total

# try to do it on one line
    # return sum(map(lambda x: int(x), arr))
    # return sum(int(n) for n in arr)
    return sum(map(int, arr))



print(sum_mix([9, 3, '7', '3']))
