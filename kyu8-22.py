def bool_to_word(boolean) :
    # return 'Yes' if boolean else 'No'

    # clever solution using True or False as index since True=1 and False=0
    return ['No', 'Yes'][boolean]
    # Another way to think of it
    # lst = ['No', 'Yes']
    # return lst[boolean]

print(bool_to_word(True))
print(bool_to_word(False))

# a change
