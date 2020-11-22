# Given an array/list [] of integers , Find The maximum difference
# between the successive elements in its sorted form.

def max_gap(numbers) :
    sorted_nums = sorted(numbers)
    lst, i, diff = [], 1, 0

    for each in sorted_nums :
        if i == len(numbers) : break

        diff = sorted_nums[i] - each
        lst.append(diff)

        i = i + 1

    return max(lst)


print(max_gap([13,10,2,9,5]))
# print(max_gap([13,3,5]))
# print(max_gap([24,299,131,14,26,25]))
# print(max_gap([-7,-42,-809,-14,-12]))
# print(max_gap([-1,-1,-1]))
