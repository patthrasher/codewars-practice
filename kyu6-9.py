import re
def is_pangram(s) :
    # first solution
    all = ''

    s = s.lower()
    x = re.findall("[a-z]", s)

    for each in x :
        if each in all : continue
        all = all + each

    return len(all) == 26

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
