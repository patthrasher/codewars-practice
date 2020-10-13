# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def areYouPlayingBanjo(name) :
    output = ''
    if name[0].lower() == 'r' :
        output = ' plays banjo'
    else :
        output = ' does not play banjo'

    return name + output



print(areYouPlayingBanjo('Pat'))
print(areYouPlayingBanjo('Rat'))
print(areYouPlayingBanjo('rat'))

print(areYouPlayingBanjo('new case!'))
