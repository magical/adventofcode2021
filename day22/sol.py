from collections import namedtuple

Cube = namedtuple("Cube", "x,y,z")

def solve(file, small=False):
    cubes = [] # nonoverlapping
    for action, cube in parse(file):
        if small and any(x > 50 or x < -50 for c in cube for x in c):
            #print("skipping", cube)
            continue
        if action == 'on':
            cubelist = [cube]
            for other in cubes:
                if overlaps_any(other, cubelist):
                    #print("overlap", other, cube, overlap_size(other, cube), overlap_region(other, cube))
                    cubelist = subtract_list(cubelist, other)
            cubes.extend(cubelist)
        elif action == 'off':
            nubes = []
            for other in cubes:
                if overlaps(other, cube):
                    #print("overlap", other, cube, overlap_size(other, cube), overlap_region(other, cube))
                    nubes.extend(subtract(other, cube))
                else:
                    nubes.append(other)
            cubes = nubes
        else:
            print("?", action,cube)
        #print(len(cubes))
    print(sum(map(cube_size, cubes)))

def overlaps_any(cube, list):
    return any(overlaps(cube, x) for x in list)

def subtract_list(list, cube):
    out = []
    for x in list:
        if overlaps(x, cube):
            out.extend(subtract(x, cube))
        else:
            out.append(x)
    return out

def subtract(a,b):
    if not overlaps(a,b):
        return [a]
    if contains(b,a):
        return []
    # slice nonoverlapping bits off of the cube until
    # all that remains is contained by b
    out = []
    rest = a
    if rest.x[0] < b.x[0]:
        out.append(rest._replace(x=(rest.x[0],b.x[0]-1)))
    if rest.x[1] > b.x[1]:
        out.append(rest._replace(x=(b.x[1]+1,rest.x[1])))
    rest = rest._replace(x=(max(rest.x[0],b.x[0]), min(rest.x[1],b.x[1])))

    if rest.y[0] < b.y[0]:
        out.append(rest._replace(y=(rest.y[0],b.y[0]-1)))
    if rest.y[1] > b.y[1]:
        out.append(rest._replace(y=(b.y[1]+1,rest.y[1])))
    rest = rest._replace(y=(max(rest.y[0],b.y[0]), min(rest.y[1],b.y[1])))

    if rest.z[0] < b.z[0]:
        out.append(rest._replace(z=(rest.z[0],b.z[0]-1)))
    if rest.z[1] > b.z[1]:
        out.append(rest._replace(z=(b.z[1]+1,rest.z[1])))
    rest = rest._replace(z=(max(rest.z[0],b.z[0]), min(rest.z[1],b.z[1])))

    assert contains(b,rest)
    return out

def parse(file):
    for line in file:
        action, coords = line.split()
        coords = [tuple(map(int, x.partition('=')[2].split('..'))) for x in coords.split(',')]
        cube = Cube(*coords)
        yield action,cube

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

def overlap_size(a,b):
    # precondition: overlaps(a,b)
    dx = overlap_1d(a.x, b.x)
    dy = overlap_1d(a.y, b.y)
    dz = overlap_1d(a.z, b.z)
    return dx*dy*dz

def overlap_1d(a,b):
    return min(a[1],b[1]) - max(a[0],b[0]) + 1

def contains(a,b):
    return (a.x[0] <= b.x[0] and b.x[1] <= a.x[1] and
            a.y[0] <= b.y[0] and b.y[1] <= a.y[1] and
            a.z[0] <= b.z[0] and b.z[1] <= a.z[1])
    

def cube_size(c):
    dx = c.x[1] - c.x[0] + 1
    dy = c.y[1] - c.y[0] + 1
    dz = c.z[1] - c.z[0] + 1
    return dx*dy*dz

solve(open("sample"),small=True)
solve(open("input"),small=True)
solve(open("sample2"))
solve(open("input"))
