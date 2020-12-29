def word_to_bin(word) :
    return ['0' + bin(ord(i))[2:] for i in word]

print(word_to_bin('man'))
