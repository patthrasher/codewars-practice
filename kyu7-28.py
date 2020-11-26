# Given an array of N integers, you have to find how many times
# you have to add up the smallest numbers in the array until their
# Sum becomes greater or equal to K.

def minimum_steps(numbers, value) :
    total, i = 0, 0

    for each in sorted(numbers) :
        total += each
        if total >= value :
            break
        i += 1

    return i


print(minimum_steps([4,6,3], 7)) # 1
print(minimum_steps([10,9,9,8], 17)) # 1
print(minimum_steps([8,9,10,4,2], 23)) # 3
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464)) # 8
