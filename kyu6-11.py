def solution(s) :
    # first solution
    # if len(s) % 2 == 1 :
    #     s = s + '_'
    # l = []
    # ns = ''
    # for each in s :
    #     ns = ns + each
    #     if len(ns) == 2 :
    #         l.append(ns)
    #         ns = ''
    # return l

    # regex solution
    import re
    s = s + '_' if len(s) % 2 == 1 else s
    return re.findall('..', s)

print(solution("asdfadsf")) # ['as', 'df', 'ad', 'sf']
print(solution("asdfads")) # ['as', 'df', 'ad', 's_']
