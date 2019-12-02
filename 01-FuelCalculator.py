import math

def main():
    lines = []
    with open("data/01-Mass.txt") as file:
        lines = file.readlines()
    
    end_total = 0
    for line in lines:
        mass = int(line)
        base_fuel = baseFuel(mass)
        
        total = base_fuel
        extra_fuel = base_fuel
        
        while(True):
            extra_fuel = math.floor(extra_fuel / 3) - 2
            if (extra_fuel <= 0):
                end_total += total
                break
            else:
                total += extra_fuel

    print("Total fuel: %s" % (end_total))

def baseFuel(mass: int) -> int:
    base_fuel = math.floor(mass / 3) - 2
    return base_fuel
    

if __name__== "__main__":
    main()
