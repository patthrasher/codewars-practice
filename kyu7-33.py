def valid_spacing(s) :
    # first solution
    # if s.startswith(' ') or s.endswith(' ') or '  ' in s :
    #     return False
    #
    # return True

    # one line solution
    # return False if s.startswith(' ') or s.endswith(' ') or '  ' in s else True

    # regular expression solution
    import re
    return False if re.search('^ ', s) or re.search(' $', s) or re.search('  ', s) else True

print(valid_spacing('Hello world')) # True
print(valid_spacing('Hello world ')) # False
print(valid_spacing('Hello  world')) # False
print(valid_spacing(' Hello world')) # False
print(valid_spacing('Hello world')) # True
