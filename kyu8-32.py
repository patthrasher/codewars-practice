def multi_table(number) :
    s = ''

    for i in range(1, 11) :
        prod = i * number
        string = str(i) + ' * ' + str(number) + ' = ' + str(prod)
        if i < 10 :
            s = s + string + '\n'

        else :
            s = s + string

    return s
    
print(multi_table(5))
