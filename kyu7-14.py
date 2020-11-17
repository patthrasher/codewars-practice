# Disarium number is the number that The sum of its digits
# powered with their respective positions is equal to the number itself.

from math import pow

def disarium_number(number) :
    s = list(enumerate(str(number), 1))
    lst = []
    for i, each in s :
        lst.append(pow(int(each), i))
        
    return 'Disarium !!' if sum(lst) == number else 'Not !!'


print(disarium_number(89))
print(disarium_number(518))
print(disarium_number(1024))
