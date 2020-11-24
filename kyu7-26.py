def row_weights(array) :
    # first solution

    # lst1 = []
    # lst2 = []
    #
    # for i, each in list(enumerate(array)) :
    #     if i % 2 == 0 :
    #         lst1.append(each)
    #     else :
    #         lst2.append(each)
    #
    # return (sum(lst1), sum(lst2))

    # second solution
    # one = sum([each for i, each in list(enumerate(array)) if i % 2 == 0])
    # two = sum([each for i, each in list(enumerate(array)) if i % 2 == 1])
    #
    # return (one, two)


    # third solution, no lists!
    one, two, i = 0, 0, 0
    for each in array :
        if i == 0 :
            one += each
            i += 1
        else :
            two += each
            i -= 1

    return (one, two)


print(row_weights([50,60,70,80]))
print(row_weights([100,51,50,100]))
print(row_weights([80]))
print(row_weights([100,50]))
