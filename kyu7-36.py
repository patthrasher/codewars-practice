def word_to_bin(word) :
    l = []
    for each in word :
        x = ord(each)
        y = bin(x)[2:]
        str = '0' + y
        l.append(str)

    return l


print(word_to_bin('man'))
