from math import sqrt

def list_squared(m, n) :
    output = []
    for each in range(m, n + 1) :
        l = []
        for i in range(1, each + 1) :
            if each % i == 0 :
                l.append(i * i)

        tot = sum(l)
        root = sqrt(tot)
        if str(root).endswith('.0') :
            output.append([each, tot])

    return output


print(list_squared(42, 250)) # [[1, 1], [42, 2500], [246, 84100]]
