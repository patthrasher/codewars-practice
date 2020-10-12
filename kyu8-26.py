def check_exam(arr1,arr2) :
    # count, score = 0, 0
    # while count < len(arr1) :
    #     if arr2[count] == '' :
    #         count = count
    #     elif arr1[count] == arr2[count] :
    #         score += 4
    #     else :
    #         score -= 1
    #     count += 1
    #
    # return score if score >= 0 else 0

    # for loop solution
    # count, score = 0, 0
    # for each in arr2 :
    #     if each == '' : pass
    #     elif each == arr1[count] : score += 4
    #     else : score -= 1
    #     count += 1
    # return score if score >=0 else 0

    # x = zip(arr1, arr2)
    # print(list(x))

    # dig this one
    score = 0

    for i in range(0, len(arr1)):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr2[i] != "":
            score -= 1
    return max(score, 0)

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
