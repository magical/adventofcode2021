import numpy as np
import random
from collections import Counter
def solve(scanner, threshold=12):
    # choose one scanner
    # for each other scanner,
    #   try every transformation
    #   sort points
    #   find the transformation which maximizes the number of overlapping points
    #
    s = scanner[0]
    s = np.array(s) # n x 3
    print(s)
    indices = list(range(1,len(scanner)))
    seen = set(map(tuple,s))
    offsets = []
    while indices:
        for i in indices:
            print("index", i)
            r = scanner[i]
            r = np.array(r)
            #print(r)
            r,offset = find_transformation(s, r)
            if r is None:
                continue
            add = [x for x in map(tuple,r) if x not in seen]
            seen.update(add)
            s = np.append(s,add,axis=0)
            offsets.append(offset)
            indices.remove(i)
            print(s.shape)
            break

    # part 1: number of unique points
    print(len(seen))

    # part 2: find the max sum of distances
    pos = np.array(offsets)
    d = pos[np.newaxis,:,:] - pos[:,np.newaxis,:]
    m = np.max(np.sum(np.abs(d), axis=2))
    print(m)

def find_transformation(s,r,threshold=12):
    try:
        score,r,offset = max(try_transformation(s,r,threshold), key=lambda x:x[0])
        print("found overlap w/", score)
        return r,offset
    except ValueError:
        return None,None


def try_transformation(s,r,threshold):
    for swap, scale in rotations:
        rr = r[:,swap]*scale
        # find the difference between every point in s and every point in r
        # duplicate by len(s)  - n x m x 3
        # outer subtract r[*,*,i] = r[*,*,:] - s[i]
        diff = np.subtract(rr[np.newaxis,:,:], s[:,np.newaxis,:])
        #assert np.all(diff[0] + s[0] == rr)
        #assert np.all(diff[1] + s[1] == rr)
        #print(diff)
        # here's the tricky part: the most common offset is the offset we want
        c = Counter(map(tuple, diff.reshape(-1,3)))
        #print(len(c))
        [(top, score)] = c.most_common(1)
        if score > 5:
            print(top, score)
        if score < threshold:
            continue
        yield score, rr - top, top

def rot():
    I = np.identity(3,dtype=int)
    for x in 1,-1:
        for y in 1,-1:
            for z in 1,-1:
                for p in [
                    [0,1,2],
                    [0,2,1],
                    [1,0,2],
                    [1,2,0],
                    [2,0,1],
                    [2,1,0],
                ]:
                    if np.linalg.det(I[:,p] * [x,y,z]) > 0.5:
                        yield p,[x,y,z]
rotations = list(rot())

def read(file):
    scanner = []
    coords = []
    for line in file:
        if not line.strip():
            continue
        if '---' in line:
            if coords:
                scanner.append(coords)
                coords = []
            continue
        coords.append(tuple(map(int,line.strip().split(','))))
    if coords:
        scanner.append(coords)
    return scanner

solve(read(open('sample')))
solve(read(open('input')))
