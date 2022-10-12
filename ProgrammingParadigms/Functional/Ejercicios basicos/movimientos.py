from math import sqrt

coord = lambda x, y: (x, y)

north = lambda coord: (coord[0], coord[1] + 1)
south = lambda coord: (coord[0], coord[1] - 1)
east = lambda coord: (coord[0] + 1, coord[1])
west = lambda coord: (coord[0] - 1, coord[1])

northeast = lambda coord: north(east(coord))
northwest = lambda coord: north(west(coord))
southeast = lambda coord: south(east(coord))
southwest = lambda coord: south(west(coord))

distance = lambda coord1, coord2: sqrt((coord2[0]-coord1[0])^2 + (coord2[1]-coord1[1])^2)

print(distance((1,2), (3,4)))