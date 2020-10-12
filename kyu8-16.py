def is_uppercase(inp) :
    # for each in inp :
    #     if each.islower() :
    #         return False
    #
    # return True

    # try to do it on one line, oh my gosh didn't even need a for loop haha
    # isupper() islower() checks the whole string 
    return inp.isupper()

print(is_uppercase('cc'))
print(is_uppercase('C'))
