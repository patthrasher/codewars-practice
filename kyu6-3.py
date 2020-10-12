def likes(names) :
    if len(names) >= 4 :
        output = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
    elif len(names) == 3 :
        output = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    elif len(names) == 2 :
        output = names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 1 :
        output = names[0] + ' likes this'
    else :
        output = 'no one likes this'

    return output

print(likes(['Max', 'John', 'Mark', 'Four']))


# cool solution
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print(likes(['Pat', 'Mal', 'Dagny', 'House']))

# another to look at
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
