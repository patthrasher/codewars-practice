# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5
# Given a number determine if it special number or not .

def special_number(number) :
    # first solution
    # lst = ['6', '7', '8', '9']
    # s = str(number)
    #
    # for each in s :
    #     if each in lst :
    #         return 'NOT!!'
    #
    # return 'Special!!'

    # second solution
    # s = str(number)
    # return ['Special!!', 'NOT!!']['6' in s or '7' in s or '8' in s or '9' in s]

    # third solution
    s, lst = str(number), ['6', '7', '8', '9']
    return ('Special!!', 'NOT!!')[any(i in s for i in lst)]

print(special_number(23))
print(special_number(39))
