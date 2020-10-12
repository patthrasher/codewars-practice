def sum_str(a, b) :
    # return str(int(a) + int(b))
    # try :
    #     a = int(a)
    # except :
    #     a = 0
    # try :
    #     b = int(b)
    # except :
    #     b = 0
    #
    # return str(a + b)

    return str(int(a or 0) + int(b or 0))




print(sum_str('', ''))
