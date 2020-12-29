def max_and_min(arr1,arr2) :
    big = None
    little = None
    for num1 in arr1 :
        for num2 in arr2 :
            if big == None or abs(num1 - num2) > big :
                big = abs(num1 - num2)
            if big == None or abs(num2 - num1) > big :
                big = abs(num2 - num1)

            if little == None or abs(num1 - num2) < little :
                little = abs(num1 - num2)
            if little == None or abs(num2 - num1) < little :
                little = abs(num2 - num1)

    return [big, little]

print(max_and_min([3,10,5],[20,7,15,8])) # [17, 2]
print(max_and_min([3],[20])) # [17, 17]
print(max_and_min([3,10,5],[3,10,5])) # [7, 0]
