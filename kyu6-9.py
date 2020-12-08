import re
def is_pangram(s) :
    all_unique = ''
    all = re.findall("[a-z]", s.lower())

    for each in all :
        if each in all_unique : continue
        all_unique += each

    return len(all_unique) == 26


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
