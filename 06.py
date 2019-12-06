with open("06.txt") as f:
    orbit_map = [line.rstrip().split(")") for line in f.readlines()]

orbit_map_dict = {orbit[1]:orbit[0] for orbit in orbit_map}

all_planets = list(set([planet for orbit in orbit_map for planet in orbit]))

centre = [planet for planet in all_planets if planet not in [planet[1] for planet in orbit_map]][0]

##PART1

def count_orbits(count, planet):
    if planet == centre:
        return count
    else:
        count += 1
        return count_orbits(count, orbit_map_dict[planet])

def count_all_orbits():
    count = 0
    for planet in all_planets:
        count = count_orbits(count, planet)
    return count

orbits = count_all_orbits()

##PART2
def trace_route(planet, route):
    if planet == centre:
        return route
    else:
        route.append(planet)
        return trace_route(orbit_map_dict[planet], route)

transefers = len(set(trace_route("YOU", []))^set(trace_route("SAN", []))) - 2
