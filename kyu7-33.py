def valid_spacing(s) :
    # first solution
    # if s.startswith(' ') or s.endswith(' ') or '  ' in s :
    #     return False
    #
    # return True

    # one line solution
    return False if s.startswith(' ') or s.endswith(' ') or '  ' in s else True


print(valid_spacing('Hello world'))
print(valid_spacing(' Hello world'))
