# Jumping number is the number that All adjacent digits in it differ by 1.

def jumping_number(number) :
    s, i = str(number), 1
    for each in s :
        if i == len(s) :
            return 'Jumping!!'
        elif int(each) == int(s[i]) - 1 or int(each) == int(s[i]) + 1 :
            i = i + 1
            
    return 'Not!!'

print(jumping_number(9))
print(jumping_number(23))
print(jumping_number(8987))
print(jumping_number(5679))
