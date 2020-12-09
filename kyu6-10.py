states = {
'AZ': 'Arizona',
'CA': 'California',
'ID': 'Idaho',
'IN': 'Indiana',
'MA': 'Massachusetts',
'OK': 'Oklahoma',
'PA': 'Pennsylvania',
'VA': 'Virginia'
}

def by_state(str) :
    # long and convoluted but it works!
    new_str = '..... '
    state_list = []
    str_list = []

    split = str.split('\n')
    for each in split :
        state = each[-2:]
        try :
            full_state = states[state]
        except :
            quit()
        if full_state not in state_list :
            state_list.append(full_state)

        no_commas = each.split(',')
        no_commas[2] = no_commas[2][:-2] + full_state

        for part in no_commas :
            new_str = new_str + part
        str_list.append(new_str)

        new_str = '..... '

    str_list = sorted(str_list)

    another_list = []
    big_str = ''
    i = 0
    for each in sorted(state_list) :
        big_str = big_str + each + '\r\n'
        for person in str_list :
            if i < len(str_list) - 1:
                if each in person :
                    big_str = big_str + person + '\r\n'
                    i = i + 1
            else :
                if each in person :
                    big_str = big_str + person

                    i = i + 1

        big_str = big_str + ' '

        another_list.append(big_str)
        big_str = ''

    s = ''
    for each in another_list :
        s = s + each

    return s[:-1]

print(by_state("""John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA"""))

print('=======================')

print(by_state("""John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
Terry Kalkas, 402 Lans Road, Beaver Falls PA
Eric Adams, 20 Post Road, Sudbury MA
Hubert Sims, 328A Brook Road, Roanoke MA
Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
Sal Carpenter, 73 6th Street, Boston MA"""))
