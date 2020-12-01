def max_multiple(divisor, bound) :
    i = bound
    while i > 0 :
        if i % divisor == 0 :
            return i
        i = i - 1



print(max_multiple(2,7)) # 6
print(max_multiple(3,10)) # 9
print(max_multiple(7,17)) # 14
