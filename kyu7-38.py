def averages(arr) :
    if arr == None or len(arr) < 2 :
        return []
    l = []
    i = 1
    while i < len(arr) :
        x = arr[i - 1] + arr[i]
        av = x / 2
        l.append(av)
        i = i + 1

    return l

print(averages([1, 3, 5, 1, -10])) # [2, 4, 3, -4.5]
