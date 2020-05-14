# Debug function getSumOfDigits that takes positive integer to calculate sum of it's digits.
# Assume that argument is an integer.

def get_sum_of_digits(num) :    
    sum = 0
    digits = list(str(num))
    for x in digits:
        sum = sum + int(x)
    return sum

print(get_sum_of_digits(1337))
