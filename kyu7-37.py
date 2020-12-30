def alternate_case(s) :
    st = ''
    for each in s :
        if each.isupper() :
            st += each.lower()
        elif each.islower() :
            st += each.upper()
        else :
            st += ' '

    return st


print(alternate_case('Hello World'))
