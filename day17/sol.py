
sample = [(20,-10),(30,-5)]
input = [(88,-157),(125,-103)]

def fire(velocity, target):
    x = 0
    y = 0
    vx, vy = velocity
    maxy = 0
    while True:
        #print(x,y, sep=",", end=" ")
        if y > maxy:
            maxy = y
        if inside(x, y, target):
            # success
            return maxy, True
        if x > target[1][0] or y < target[0][1]:
            # will never hit target
            return 0, False
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1

def brute(target):
    best = (0,0)
    maxy = 0
    count = 0
    for x in range(0,target[1][0]+1):
        for y in range(target[0][1],abs(target[0][1])+1):
            height, ok = fire((x,y), target)
            if ok:
                count += 1
                if height > maxy:
                    maxy = height
                    best = x,y
    print(best,maxy, count)
    return maxy

def sign(v):
    if v > 0: return 1
    if v < 0: return -1
    return 0

def inside(x,y,box):
    return box[0][0] <= x <= box[1][0] and box[0][1] <= y <= box[1][1]

print(fire((6,3), sample))
print(fire((6,9), sample))
print(brute(sample))
print(brute(input))
