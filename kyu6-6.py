def meeting(s) :
    count = 0
    how_many_names = s.count(':')

    fn = []
    ln = []

    while count < how_many_names :

        x = s.find(':')
        y = s.find(';')

        fn.append(s[:x].upper())

        ln_range = s[x+1:y]
        if y == -1 :
            ln_range = s[x+1:]

        ln.append(ln_range.upper())

        s = s[y + 1:]
        count = count + 1

    zippy = sorted(list(zip(ln, fn)))

    new_str = ''
    for first, last in zippy :
        new_str += '(' + first + ', ' + last + ')'

    return(new_str)

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))
