# Given an array of integers , Find the minimum sum which
# is obtained from summing each Two integers product .

def min_sum(arr) :
    lst = []

    while len(arr) > 0 :
        mx = max(arr)
        mn = min(arr)
        lst.append(mx * mn)

        arr.remove(mx)
        arr.remove(mn)

    return sum(lst)

print(min_sum([5,4,2,3]))
print(min_sum([12,6,10,26,3,24]))
