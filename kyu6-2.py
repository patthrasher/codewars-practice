# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure)
# that checks whether the two arrays have the "same" elements,
# with the same multiplicities. "Same" means, here, that the elements in b are the
# elements in a squared, regardless of the order.

def comp(array1, array2) :
    if len(array1) == 0 or len(array2) == 0 :
        return False

    counter = 0
    for each in array1 :
        square = each * each

        for test in array2 :
            if square == test :
                counter = counter + 1
                break

    if len(array1) == len(array2) and len(array2) == counter :
        return True

    return False
