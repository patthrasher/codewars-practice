def minimum_number(numbers) :

    start = sum(numbers)
    end = start + 50

    for i in range(start, end) :
        if i > 1 :
            for j in range(2, i) :
                if(i % j == 0) :
                    break
            else:
                prime = i
                real = prime - start
                break

    return real




print(minimum_number([3,1,2]))
print(minimum_number([1,1,1]))
print(minimum_number([2,12,8,4,6]))
print(minimum_number([50,39,49,6,17,28]))
