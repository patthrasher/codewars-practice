# Given an array of integers , Find the maximum product obtained
# from multiplying 2 adjacent numbers in the array.

def adjacent_element_product(array) :
    big = None
    for each in zip(array, array[1:]) :
        prod = each[0] * each[1]
        if big == None or prod > big :
            big = prod

    return big


print(adjacent_element_product([1, 5, 10, 9]))
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))
print(adjacent_element_product([3, 6, -2, -5, 7, 3]))
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))
