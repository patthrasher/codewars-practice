# Balanced number is the number that * The sum of all digits to
# the left of the middle digit(s) and the sum of all digits to
# the right of the middle digit(s) are equal*.
# Find if number is balanced

def balanced_num(number) :
    strnum = str(number)

    l = len(strnum)

    left = []
    right = []

    if l % 2 == 0 :
        #two numbers in middle
        print('two middle')
        half = int(l / 2 - 1)
        # print(half)

        for each in strnum[:half] :
            left.append(int(each))

        for each in strnum[half + 2:] :
            right.append(int(each))

    else :
        #one number in middle
        print('one middle')
        half = int(l / 2 - .5)
        # print(half)

        for each in strnum[:half] :
            left.append(int(each))

        for each in strnum[half + 1:] :
            right.append(int(each))

    print(sum(left))
    print(sum(right))

    if sum(left) == sum(right) :
        return 'Balanced'
    else :
        return 'Not Balanced'


print(balanced_num(19519))
print(balanced_num(123312))
