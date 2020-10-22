# Write a function called repeat_str which repeats
# the given string src exactly count times.

def repeat_str(repeat, string) :
    return string * repeat

# lambda solution
# repeat_str = lambda repeat, string: repeat * string

print(repeat_str(6, "I"))
print(repeat_str(5, "Hello"))
