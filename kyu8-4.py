# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

def abbrevName(name) :
    split = name.split()
    return split[0][0].upper() + '.' + split[1][0].upper()

    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

    return '.'.join(w[0] for w in name.split()).upper()

    lst = [1, 2, 3]
    [print(i) for i in lst]

print(abbrevName('nate bargatze'))
