# A number is called Automorphic number if and only if its
# square ends in the same digits as the number itself.

def automorphic(n) :
    # first solution
    # x = n ** 2
    # s = str(n)
    # sq = str(x)
    #
    # if s == sq[-len(s):] :
    #     return 'Automorphic'
    # else :
    #     return 'Not!!'

    # second solution, one line!
    return 'Automorphic' if str(n) == str(n**2)[-len(str(n)):] else 'Not!!'

    # though I'd probably prefer str(n) its own variable
    # s = str(n)
    # return 'Automorphic' if s == str(n**2)[-len(s):] else 'Not!!'

    # dang could have used endswith()!
    # return 'Automorphic' if str(n**2).endswith(str(n)) else 'Not!!'


print(automorphic(25))
print(automorphic(76))
print(automorphic(625))
print(automorphic(26))
print(automorphic(353))
