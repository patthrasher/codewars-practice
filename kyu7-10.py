# In this Kata, you will be given an array of numbers in which two numbers
# occur once and the rest occur only twice. Your task will be to return the
# sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8
# occur once, and their sum is 15.

# first solution
# def repeats(arr) :
#     new_lst = []
#     for each in arr :
#         if arr.count(each) == 1 :
#             new_lst.append(each)
#
#     return sum(new_lst)

# list comprehension
# def repeats(arr) :
#     return sum([i for i in arr if arr.count(i) == 1])

# apparently didn't need the brackets, neat
def repeats(arr) :
    return sum(i for i in arr if arr.count(i) == 1)

print(repeats([4,5,7,5,4,8]))
