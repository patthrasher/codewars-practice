def zero_fuel(distance_to_pump, mpg, fuel_left) :
    if mpg * fuel_left < distance_to_pump :
        return False

    return True

print(zero_fuel(50, 25, 2))

# second attempt before looking at other solutions, got it on one line!
def zero_fuel2(d, m, f) :
    return m * f >= d

print(zero_fuel2(50, 25, 1))

# lambda solution
zeroFuel = lambda distance, mpg, gallons: mpg * gallons >= distance

print(zeroFuel(90, 3, 100))
