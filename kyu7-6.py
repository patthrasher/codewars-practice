def round_to_next5(n) :
    # return n + (5 - n) % 5

    # recursive solution
    return n if n%5 == 0 else round_to_next5(n+1)


print(round_to_next5(-12))
