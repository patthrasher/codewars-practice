def get_strings(city) :

    strs = ''
    str_list = []
    lst = [i for i in city.lower() if i.isalpha()]

    for each in lst :
        count = lst.count(each)
        ast = '*' * count

        if each not in strs :
            strs = strs + each
            each_str = each + ':' + ast
            str_list.append(each_str)

    final_str = ','.join(str_list)

    return final_str

# didn't need lists on mine!
    # city = city.lower()
    # result = ""
    # for i in city:
    #     if i in result:
    #         pass
    #     elif i == " ":
    #         pass
    #     else:
    #         result += i + ":" + ("*" * city.count(i)) + ","
    #
    # return result[:-1]

print(get_strings('Chicago'))
print(get_strings('Bangkok'))
print(get_strings('New York'))
