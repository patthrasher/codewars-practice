def smallest(n) :
    # strn = str(n)
    #
    # i = 0
    # smallest = None
    # for each in strn :
    #     # print('i', i)
    #     if smallest is None or int(each) < smallest :
    #         smallest = int(each)
    #         place = i
    #         # print(smallest)
    #     i = i + 1
    #
    # # print(smallest, place)
    #
    # strn = list(strn)
    #
    # x = strn.pop(place)
    # strn.insert(0, x)
    #
    # # print(strn)
    #
    # new_str = ''.join(strn)
    # print(new_str)

# nice solution here
    s = str(n)
    min1, from1, to1 = n, 0, 0
    for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        print('removed', removed)
        for j in range(len(removed)+1):
            num = int(removed[:j] + s[i] + removed[j:])
            print('num', num)
            if (num < min1):
                min1, from1, to1 = num, i, j
    return [min1, from1, to1]

print(smallest(2341))
# print(smallest(1035))
# print(smallest(900))
