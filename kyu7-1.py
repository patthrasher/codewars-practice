# Create a function named divisors/Divisors that takes an integer n > 1
# and returns an array with all of the integer's divisors(except for 1 and
# the number itself), from smallest to largest. If the number is prime return
# the string '(integer) is prime' (null in C#) (use Either String a in Haskell
# and Result<Vec<u32>, String> in Rust).

def divisors(integer) :
    lst = []
    index = 2
    while index < (integer + 1) / 2 :
        case = integer % index
        if case == 0 :
            lst.append(index)
        index = index + 1

    if len(lst) == 0 :
        return str(integer) + ' is prime'
    else :
        return lst

print(divisors(5))
