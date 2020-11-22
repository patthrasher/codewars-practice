# An element is leader if it is greater than The Sum all the elements to its right side.

def array_leaders(numbers) :
    lst = []
    i = 1
    for each in numbers :
        x = sum(numbers[i:])

        if each > x :
            lst.append(each)

        i = i + 1

    return lst




print(array_leaders([1,2,3,4,0]))
print(array_leaders([16,17,4,3,5,2]))
print(array_leaders([-1,-29,-26,-2]))
print(array_leaders([5,2]))
print(array_leaders([0,-1,-29,3,2]))
