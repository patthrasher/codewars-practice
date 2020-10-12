def reverse_bits(n) :
    # binary = bin(n)[2:]
    #
    # lst1 = [i for i in binary]
    # lst2 = []
    #
    # for each in lst1 :
    #     lst2.insert(0, each)
    #
    # reversed = ''.join([i for i in lst2])
    #
    # new_number = int(reversed, 2)
    #
    # return new_number

    # with slick reverse slice!
    # binary = bin(n)[2:]
    # reverse = binary[::-1]
    # new = int(reverse, 2)
    # return new

    # try to make it shorter
    # binary = bin(n)[2:]
    # return int(binary[::-1], 2)

    # and shorter?
    # return int(bin(n)[2:][::-1], 2)

    # not shorter still!?
    return int(bin(n)[:1:-1], 2)




print(reverse_bits(417))
# print(reverse_bits(267))
