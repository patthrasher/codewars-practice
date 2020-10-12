def greet(name) :
    # return "Hello, " + name + " how are you doing today?"

    # return "Hello, {} how are you doing today".format(name)

    # f string literal availalbe in python 3.6 and later
    return f'Hello, {name} how are you doing today'

print(greet('Pat'))
