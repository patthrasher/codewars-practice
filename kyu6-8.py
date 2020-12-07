def sum_arrays(array1,array2) :
    # first solution, pretty ugly but works haha
    if len(array1) == 0 and len(array2) == 0 :
        return []

    elif len(array1) > 0 and len(array2) == 0 :
        one = int(''.join([str(i) for i in array1]))
        two = 0

    elif len(array1) == 0 and len(array2) > 0 :
        one = 0
        two = int(''.join([str(i) for i in array2]))

    else :
        one = int(''.join([str(i) for i in array1]))
        two = int(''.join([str(i) for i in array2]))

    if str(one).startswith('-') or str(two).startswith('-') :

        lst = []
        x = str(one + two)
        index_at = 0
        if int(x) > 0 :
            index_at = 1
        else :
            index_at = 2

        lst.append(int(x[:index_at]))
        for each in x[index_at:] :
            lst.append(int(each))

        return lst

    else :
        return list(int(i) for i in (str(sum([one, two]))))

print(sum_arrays([3,2,9],[1,2])) # [3, 4, 1]
print(sum_arrays([4,7,3],[1,2,3])) # [5, 9, 6]
print(sum_arrays([],[])) # []
print(sum_arrays([0],[])) # [0]
print(sum_arrays([3,2,6,6],[-7,2,2,8])) # [-3, 9, 6, 2]
print(sum_arrays([0, 1, 4, 8, 4],[])) # [1, 4, 8, 4]
print(sum_arrays([-4, 8, 6], [8, 2, 7, 1, 1])) # [8, 2, 2, 2, 5]
print(sum_arrays([], [0, 4, 5, 2])) # [4, 5, 2]
