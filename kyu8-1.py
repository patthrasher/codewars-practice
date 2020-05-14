# Given three integers a ,b ,c, return the largest number obtained
# after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

def expression_matter(a, b, c) :
    options = [a + b + c, a * b * c, a + b * c, a * b + c, (a + b) + c,
        (a + b) * c, (a * b) * c, a + (b + c), a * (b + c), a * (b * c)]

    highest = 0
    for each in options :
        print(each)
        if each > highest :
            highest = each

    return highest

print(expression_matter(2, 2, 3))
