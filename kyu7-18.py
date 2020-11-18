# Extra perfect number is the number that first and last bits are set bits.
# Given a positive integer N , Return the extra perfect numbers in range from 1 to N .

def extra_perfect(n) :
    lst = []
    for each in range(1, n + 1) :
        if str(bin(each)[2:]).startswith('1') and bin(each).endswith('1') :
            lst.append(each)

    return lst

print(extra_perfect(3))
print(extra_perfect(7))
print(extra_perfect(28))
