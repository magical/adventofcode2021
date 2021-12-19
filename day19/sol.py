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
    while indices:
        for i in indices:
            print("index", i)
            r = scanner[i]
            r = np.array(r)
            #print(r)
            r = find_transformation(s, r)
            if r is None:
                continue
            seen = set(map(tuple,s))
            add = [x for x in map(tuple,r) if x not in seen]
            s = np.append(s,add,axis=0)
            indices.remove(i)
            print(s.shape)
            break

def find_transformation(s,r,threshold=12):
    try:
        score,r = max(try_transformation(s,r), key=lambda x:x[0])
        print("found overlap w/", score)
        return r
    except ValueError:
        return None


def try_transformation(s,r,threshold=12):
    for r in transformations(r):
        # find the difference between every point in s and every point in r
        # duplicate by len(s)  - n x m x 3
        # outer subtract r[*,*,i] = r[*,*,:] - s[i]
        diff = np.subtract(r[np.newaxis,:,:], s[:,np.newaxis,:])
        assert np.all(diff[0] + s[0] == r)
        assert np.all(diff[1] + s[1] == r)
        #print(diff)
        # here's the tricoky part: the most common offset is the offset we want
        c = Counter(map(tuple, diff.reshape(-1,3)))
        #print(len(c))
        [(top, score)] = c.most_common(1)
        if score > 5:
            print(top, score)
        if score < threshold:
            continue
        yield score, r - top

def transformations(r):
    r = np.array(r)
    for x in 1,-1:
        for y in 1,-1:
            for z in 1,-1:
                r2 = r * [x,y,z]
                yield r2 # 0,1,2
                yield r2[:,[0,2,1]]
                yield r2[:,[1,0,2]]
                yield r2[:,[1,2,0]]
                yield r2[:,[2,0,1]]
                yield r2[:,[2,1,0]]

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
