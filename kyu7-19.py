# A Tidy number is a number whose digits are in non-decreasing order.
# Given a number, Find if it is Tidy or not .


def tidy_number(n) :
    # first solution
    s = str(n)

    i = 1
    for each in s :
        if i == len(s) :
            return True
        elif int(s[i]) < int(each) :
            return False

        i = i + 1

    # solution with zip and all
    # s = str(n)
    # return all(a<=b for a,b in zip(s,s[1:]))

    # solution with sort()
    # s = list(str(n))
    # return s == sorted(s)

print(tidy_number(1234))
print(tidy_number(12167))
