def valid_spacing(s) :
    if s.startswith(' ') or s.endswith(' ') or '  ' in s :
        return False

    return True


print(valid_spacing('Hello world'))
print(valid_spacing(' Hello world'))
