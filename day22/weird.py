from collections import namedtuple

Cube = namedtuple("Cube", "x,y,z")

def total_volume(cubes):
    print("total_volume", len(cubes))
    cubes.sort(key=cube_size, reverse=True)
    # the total volume of a set of cubes is
    # the sum of the individual volumes,
    # minus the total overlap between any two cubes
    if not cubes:
        return 0
    sum_of_volumes = 0
    overlap = []
    for i,cube in enumerate(cubes):
        if any(contains(other, cube) for other in cubes[:i]):
            continue
        sum_of_volumes += cube_size(cube)
        for other in cubes[:i]:
            if overlaps(other, cube):
                overlap.append(Cube(*overlap_region(cube, other)))
    overlap_volume = total_volume(overlap)
    #print(sum_of_volumes, overlap_volume)
    #print(overlap)
    return sum_of_volumes - overlap_volume

def overlaps(a, b):
    if (a.x[1] < b.x[0] or a.x[0] > b.x[1] or
        a.y[1] < b.y[0] or a.y[0] > b.y[1] or
        a.z[1] < b.z[0] or a.z[0] > b.z[1]):
        return False
    return True

def overlap_region(a,b):
    # precondition: overlaps(a,b)
    return [
        (max(a.x[0],b.x[0]), min(a.x[1],b.x[1])),
        (max(a.y[0],b.y[0]), min(a.y[1],b.y[1])),
        (max(a.z[0],b.z[0]), min(a.z[1],b.z[1])),
    ]

def contains(a,b):
    return (a.x[0] <= b.x[0] and b.x[1] <= a.x[1] and
            a.y[0] <= b.y[0] and b.y[1] <= a.y[1] and
            a.z[0] <= b.z[0] and b.z[1] <= a.z[1])
    

def cube_size(c):
    dx = c.x[1] - c.x[0] + 1
    dy = c.y[1] - c.y[0] + 1
    dz = c.z[1] - c.z[0] + 1
    return dx*dy*dz

print("want=",total_volume([
    Cube((-10,10),(-10,10),(0,0)),
]))
# this works...
print("=",total_volume([
    Cube((-10,5),(-10,5),(0,0)),
    Cube((-5,10),(-10,5),(0,0)),
    Cube((-10,5),(-5,10),(0,0)),
    Cube((-5,10),(-5,10),(0,0)),
]))
# but make the first shape a little bigger...
print("=",total_volume([
    Cube((-10, 6 ),(-10,5),(0,0)),
    Cube((-5,10),(-10,5),(0,0)),
    Cube((-10,5),(-5,10),(0,0)),
    Cube((-5,10),(-5,10),(0,0)),
]))
# and it gets the wrong answer
