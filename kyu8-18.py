months = {1 : 1, 2 : 1, 3 : 1, 4 : 2, 5 : 2, 6 : 2,
        7 : 3, 8 : 3, 9 : 3, 10 : 4, 11 : 4, 12 : 4}

def quarter_of(month) :
    # return months.get(month, 'Enter a month')

    # clever mathy sollution
    return (month + 2) // 3



print(quarter_of(7))
