def max_tri_sum(numbers) :
    # first solution
    # nums = numbers
    # lst = []
    #
    # while len(lst) < 3 :
    #     mx = max(nums)
    #     lst.append(mx)
    #
    #     for each in nums :
    #         if each == mx :
    #             nums.remove(each)
    #
    # return sum(lst)


    # sets can't have repeating elements!!!
    return sum(sorted(set(numbers))[-3:])


print(max_tri_sum([3,2,6,8,2,3])) # 17
print(max_tri_sum([2,9,13,10,5,2,9,5])) # 32
print(max_tri_sum([-3,-27,-4,-2,-27,-2])) # -9
