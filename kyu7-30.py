# Given an array/list [] of integers , Find the Nth smallest
# element in this array of integers

def nth_smallest(arr, pos) :
    return sorted(arr)[pos - 1]

print(nth_smallest([15,20,7,10,4,3], 3))
print(nth_smallest([-5,-1,-6,-18], 4))
print(nth_smallest([2,169,13,-5,0,-1], 4))
print(nth_smallest([-2999, 48, -38, -6840, -2692, -2114, 2, 5919, 187, 452, -85, 9969, 48], 11))
