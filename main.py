import math
def fuel_to_add(current_gallons, required_liters):
    # make the math or calculation
    galon_left = math.ceil((required_liters - current_gallons*3.78541)/3.78541)
    # return the right value
    return galon_left if galon_left > 0 else 0 

if __name__ == '__main__':
    print(fuel_to_add(0, 1))
    print('------')
    print(fuel_to_add(5, 40))
    print('------')
    print(fuel_to_add(10, 30))
    print('------')
    print( fuel_to_add(896, 20500))
    print('------')
    print(fuel_to_add(1000, 50000))