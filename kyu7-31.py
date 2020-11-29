from collections import deque

def pendulum(values) :

    # first solution, works but too slow
    # l = []
    # i = 0
    # for each in sorted(values) :
    #     if i == 0 :
    #         l.insert(0, each)
    #         i = i + 1
    #     else :
    #         l.append(each)
    #         i = i - 1
    #
    # return l


    # wow, solution using indexes
    # s = sorted(values)
    # return s[::2][::-1] + s[1::2]

    # solution using double ended que, neat
    x = deque()
    v = sorted(values)
    for i, n in enumerate(v):
        x.append(n) if i%2 else x.appendleft(n)
    return list(x)




print(pendulum([4,6,8,7,5]))
print(pendulum([-9,-2,-10,-6]))
