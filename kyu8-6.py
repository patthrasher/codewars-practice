# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

def past(h, m, s) :
    return ((h * 36000) + (m * 60) + s) * 1000

print(past(0, 1, 1))


lst = ['one','two','three']

def count(x) :
    return len(x)

y = map(count, lst)

print(y)
print(list(y))

def counter(z) :
    return list(map(lambda u: len(u), z))

print(counter(['ones', 'twos', 'threes']))

def cou(t) :
    return list(map(lambda x: x * 3, t))

print('should be 15, 18, 21', cou([5,6,7]))

def c(nums) :
    return set(map(lambda p: p * p, nums))

print(c((1,2,3)))
