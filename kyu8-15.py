# It takes two bullets to defeat one dragon, will you have enough bullets?

def hero(bullets, dragons) :
    # return bullets / dragons >= 2

    # apparently multiplication is better than division (maybe cause it keeps it as
    # an integer instead of converting to a floating point)
    return bullets >= dragons * 2



print(hero(10, 5))
print(hero(7, 4))
