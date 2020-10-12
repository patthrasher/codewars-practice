def capitalize(s, ind) :
    # new_str = ''
    # count = 0
    # for each in s :
    #     if count in ind :
    #         new_str += s[count].upper()
    #     else :
    #         new_str += s[count]
    #     count += 1
    #
    # return new_str
    # ind = set(ind)
    # return ''.join(c.upper() if i in ind else c for i,c in enumerate(s))

print(capitalize("abcdef", [1,2,5,10]))
print(capitalize("abcdef", [1,2,5,50]))
print(capitalize("abracadabra", [2,6,9,10]))
