# def sum_pairs(ints, s) :

# working solution but times out and ugly

    # lst = []
    # for each in ints :
    #     for eacher in ints[ints.index(each) + 1:] :
    #         summ = each + eacher
    #         # print('sommmmmmm', [ints.index(each), ints.index(eacher, each)])
    #
    #         if summ == s :
    #             try :
    #                 lst.append([ints.index(each), ints.index(eacher, each)])
    #             except :
    #                 lst.append([ints.index(each), ints.index(eacher)])
    #
    # # print('list', lst)
    #
    # if len(lst) > 1 :
    #     low = lst[0][1]
    #     lowest = lst[0]
    #     for each in lst :
    #         if each[1] < low :
    #             low = each[1]
    #             lowest = each
    #
    #     # print(low)
    #     # print(lowest)
    #
    #     actual = [ints[lowest[0]], ints[lowest[1]]]
    #
    #     # print(actual)
    #
    #     return actual
    #
    # else :
    #     if len(lst) > 0 :
    #         actual = [ints[lst[0][0]], ints[lst[0][1]]]
    #         return actual
    #     else :
    #         return None


# still too slow.. not even a working solution haha
    # for each in ints :
    #     x = s - each
    #     # print(x)
    #     if x in ints :
    #         return [each, x]


# top solution on codewars
    # cache = set()
    # print(cache)
    # for each in ints:
    #     if s - each in cache:
    #         print('its in', cache)
    #         return [s - each, each]
    #     cache.add(each)
    #     print('its not in so add', cache)

























# practice

def sum_pairs(ints, s) :
    cache = set()
    for each in ints :
        x = s - each # don't need to make a variable
        if x in cache :
            return [x, each]
        cache.add(each)




print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
print(sum_pairs([20, -13, 40], -7))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([5, 9, 13, -3], 10))
