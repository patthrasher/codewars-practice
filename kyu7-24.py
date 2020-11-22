# Given an array/list [] of integers , Construct a product
# array Of same size Such That prod[i] is equal to The Product
# of all the elements of Arr[] except Arr[i].

def product_array(numbers) :
    # first solution, had trouble with this one!
    # lst = []
    # i = 0
    # print('orig', numbers)
    # for each in numbers :
    #     prod = 1
    #     popped = numbers.pop(i)
    #     print('after pop', numbers)
    #     print('popped value', popped)
    #     for each in numbers :
    #         prod *= each
    #
    #     print('product', prod)
    #     lst.append(prod)
    #     numbers.insert(i, popped)
    #     print('after insert', numbers)
    #     i += 1
    #
    # return lst

    nums = numbers
    lst = []
    i = 0
    for each in nums :
        prod = 1
        popped = nums.pop(i)
        for each in nums :
            prod *= each

        lst.append(prod)
        nums.insert(i, popped)

        i += 1

    return lst


print(product_array([1,5,2]))
print(product_array([12,20]))
print(product_array([13,10,5,2,9]))
