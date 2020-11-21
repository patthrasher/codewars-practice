# Given an array/list [] of integers , Find the product of the k maximal numbers.

def max_product(lst, n) :
    # first solution, works but too slow
    # new_lst = []
    # while len(new_lst) < n :
    #     new_lst.append(max(lst))
    #     lst.remove(max(lst))
    #
    # tot = 1
    # for each in new_lst :
    #     tot = tot * each
    #
    # return tot

    # second solution without creating list, also too slow
    # i = 0
    # t = 1
    # while i < n :
    #     m = max(lst)
    #     t = t * m
    #     lst.remove(m)
    #     i = i + 1
    #
    # return t

    third solution, works and passed
    s = sorted(lst)
    total = 1
    for each in s[-n:] :
        total = total * each

    return total


print(max_product([4,3,5], 2))
print(max_product([10,8,7,9], 3))
