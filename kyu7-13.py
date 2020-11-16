# Strong number is the number that the sum of the factorial
# of its digits is equal to number itself.


def product(l) :
    total = 1
    for each in l :
        total = total * each
    return total

def strong_num(number) : # solution I submitted
    s = str(number)
    ranges = [range(1, int(i) + 1) for i in s]
    totals = [product(list(map(int, i))) for i in ranges]
    return 'STRONG!!!!' if sum(totals) == number else 'Not Strong !!'

    # first solution
    # x = str(number)
    # lst = []
    # for each in x :
    #     tot = 1
    #     for eacher in range(1, int(each) + 1) :
    #         tot = tot * eacher
    #
    #     lst.append(tot)
    #
    # if sum(lst) == number :
    #     return 'STRONG!!!!'
    # else :
    #     return 'Not Strong !!'

print(strong_num(1))
print(strong_num(145))
print(strong_num(45))
print(strong_num(2))
