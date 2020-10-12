# funny hello world program using fstring

def greet() :
    words = {'greeting' : 'hello', 'to_whom' : 'world' , 'punctuation' : '!'}
    return f"{words['greeting']} {words['to_whom']}{words['punctuation']}"

print(greet())
