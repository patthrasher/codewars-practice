def get_char(c) :
    return chr(c)

# lambda version
#get_char = lambda c: chr(c)

# found out it doesn't even need the lambda! Since it is already a function, just assign it to the new name
get_char = chr

print(get_char(65))
