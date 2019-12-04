mass = [int(int(line.strip())/3)-2 for line in open("01.txt")]

def calculate_fuel_fuel(mass):
    masses = [mass]
    new_mass = int(mass/3) - 2
    while new_mass > 0:
        masses.append(new_mass)
        new_mass = int(new_mass/3) - 2
    return sum(masses)

total_mass = sum([calculate_fuel_fuel(mass) for mass in mass])
