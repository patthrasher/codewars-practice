def next_id(arr) :
# first solution
    # if len(arr) is 0 :
    #     return 0
    #
    # lst = []
    # for each in range(len(arr)) :
    #     if each in arr :
    #         pass
    #     else :
    #         lst.append(each)
    #
    # if len(lst) is 0 :
    #     output = max(arr) + 1
    # else :
    #     output = min(lst)
    #
    # return output

# second solution
    if len(arr) is 0 :
        return 0
    better way to write the above!
    if not arr :
        return 0

    lst = [i for i in range(len(arr)) if i not in arr]

    if len(lst) is 0 :
        output = max(arr) + 1
    else :
        output = min(lst)
    
    return output

# good solution from codewars
    # for i in range(len(arr)+1):
    #     if i not in arr:
    #         return i

# and another good one
    count = 0
    while count in arr:
        count = count + 1
    return count

print(next_id([0,1,2,3,5]))
print(next_id([0,1,2,3]))
print(next_id([]))
