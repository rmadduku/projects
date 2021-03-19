import math
def length_from_two_points(x1, y1, z1, x2, y2, z2):
    length = math.abs(x1-x2)
    height = math.abs(y1-y2)
    depth = math.abs(z1-z2)
    ans = math.sqrt(length*length+height*height+depth*depth)
    return ans

def biomass_from_two_points(x1, y1, z1, x2, y2, z2, density):
    length = math.abs(x1-x2)
    width = math.abs(y1-y2)
    depth = math.abs(z1-z2)
    volume = length*width*depth
    return volume/density

# points 3 and 4 will be the top and bottom fins of the fish
def length_from_four_points(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    length = math.abs(x1-x2)
    height = math.abs(y3-y4)
    depth = (math.abs(z1-z2)+math.abs(z3-z4))/2
    ans = math.sqrt(length * length + height * height + depth * depth)
    return ans

# points 3 and 4 will be the top and bottom fins of the fish
def biomass_from_four_points(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, density):
    length = math.abs(x1-x2)
    height = math.abs(y3-y4)
    depth = (math.abs(z1-z2)+math.abs(z3-z4))/2
    volume = length*depth*height
    return volume/density
