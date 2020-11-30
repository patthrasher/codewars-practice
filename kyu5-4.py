# We will write a function gap with parameters:
# g (integer >= 2) which indicates the gap we are looking for
# m (integer > 2) which gives the start of the search (m inclusive)
# n (integer >= m) which gives the end of the search (n inclusive)

# def gap(g, m, n) :

    # first solution, works but times out
    # l = []
    # for i in range(m, n + 1) :
    #     for j in range(2, i) :
    #         if i % j == 0 :
    #             break
    #     else :
    #         l.append(i)
    #
    # for a, b in zip(l, l[1:]) :
    #     if b - a == g :
    #         return [a, b]

# second solution which works and is optimized enough to pass all tests. Had to look
# at testing primality on wikipedia, borrowed is_prime function from there. Appears the
# time out issue was due to my own prime function in first solution

def is_prime(n) :
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gap(g, m, n) :
    l = []
    for i in range(m, n + 1) :
        if is_prime(i) :
            l.append(i)
            if len(l) == 2 :
                gap = l[1] - l[0]
                if gap == g :
                    return l
                else :
                    l.remove(l[0])

print(gap(2, 3, 50)) # [3, 5]
print(gap(2,100,110)) # [101, 103]
print(gap(8,300,400)) # [359, 367]
print(gap(2,100,103)) # [101, 103]
