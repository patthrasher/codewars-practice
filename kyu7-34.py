def hex_color(codes) :
    #rgb
    if codes == '' or codes == '000 000 000' :
        return 'black'

    lst = codes.split(' ')
    m = list(map(int, lst))

    if m[0] == m[1] and m[0] == m[2] :
        return 'white'

    elif m[0] == m[1] and m[2] < m[0]:
        return 'yellow'

    elif m[0] == m[2] and m[1] < m[0]:
        return 'magenta'

    elif m[1] == m[2] and m[0] < m[1]:
        return 'cyan'

    else :
        i = m.index(max(m))

        if i == 0 :
            return 'red'
        elif i == 1 :
            return 'green'
        else :
            return 'blue'

print(hex_color('121 245 255')) # blue
print(hex_color('255 000 000')) # red
