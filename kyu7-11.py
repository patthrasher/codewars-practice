# You are given a list of unique integers arr, and two integers a and b.
# Your task is to find out whether or not a and b appear consecutively in
# arr, and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.

def consecutive(arr, a, b) :
    # return arr.index(a) + 1 == arr.index(b) or arr.index(a) - 1 == arr.index(b)

    x, y = arr.index(a), arr.index(b)
    return x + 1 == y or x - 1 == y

print(consecutive([1, 3, 5, 7], 3, 7))
print(consecutive([1, 3, 5, 7], 3, 1))
