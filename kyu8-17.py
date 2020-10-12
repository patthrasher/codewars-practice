def get_drink_by_profession(param) :
    profs = {
        "Jabroni" : "Patron Tequila",
        "School Counselor" : "Anything with Alcohol",
        "Programmer" : "Hipster Craft Beer",
        "Bike Gang Member" : "Moonshine",
        "Politician" : "Your tax dollars",
        "Rapper" : "Cristal"
    }

    # param = param.title()
    #
    # if param in profs :
    #     return profs[param]
    #
    # else :
    #     return 'Beer'

    # trying to make more concise
    param = param.title()
    return profs[param] if param in profs else 'Beer'


print(get_drink_by_profession('bike gang member'))
