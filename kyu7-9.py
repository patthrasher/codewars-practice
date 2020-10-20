# You will be given two strings a and b consisting of lower case letters,
# but a will have at most one asterix character.
# The asterix (if any) can be replaced with an arbitrary sequence (possibly empty)
# of lowercase letters. No other character of string a can be replaced.
# If it is possible to replace the asterix in a to obtain string b, then string b
# matches the pattern.
# If the string matches, return true else false.

# passes most tests, needs some work
def solve(a,b) :
    if a == b or a == '*' :
        return True
    x = a.find('*')
    # print(x)

    if a[:x] == b[:x] :
        # print('yaya')
        if a[-1] == '*' :
            return True

        for each in b[x:] :
            if each == a[x + 1] :
                y = b.find(each)
                return a[x + 1:] == b[y:]


    return False


print(solve("code*s","codewars"))
print(solve("codewar*s","codewars"))
print(solve("codewars","codewars"))
print(solve("a","b"))
print(solve("*", "codewars"))
print(solve("code*warrior","codewars"))
print(solve("s*","s"))
print(solve("aaa*","aa"))
