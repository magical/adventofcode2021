import numpy as np
import random
from collections import Counter

def solve(scanner, threshold=12):
    # compute rotation & offset invariant signatures of each scanner's beacons
    def sig(s):
        s = np.array(s)
        diff = np.subtract(s[np.newaxis,:,:], s[:,np.newaxis,:])
        diff = diff[~np.eye(diff.shape[0], diff.shape[1], dtype=bool)] # flatten and ignore diagonal
        #diff = diff.reshape(-1,3)
        return sorted(np.sum(np.abs(diff)**3, axis=1))

    sigs = [sig(r) for r in scanner]

    def incommon(a,b):
        i = j = 0
        count = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                count += 1
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
        return count

    # construct adjacency matrix of overlapping scanners
    overlaps = np.zeros((len(scanner),len(scanner)), dtype=int)
    for i in range(len(scanner)):
        for j in range(len(scanner)):
            if i < j:
                overlaps[i][j] = overlaps[j][i] = incommon(sigs[i], sigs[j])
    #print(overlaps)
    overlaps = (overlaps >= threshold * (threshold-1))
    print(overlaps.astype(int))

    # start with a single scanner,
    # for each remaining scanner,
    # pick and already-processed scanner that it overlaps with
    # and try all possible rotations to align them

    ss = [np.array(scanner[0])] # n x 3
    #print(ss)

    indices = list(range(1,len(scanner)))
    done = [0]
    offsets = []
    while indices:
        pair = None
        for i in indices:
            for j,x in zip(done,ss):
                if overlaps[i][j]:
                    s = x
                    pair = i,j
        if not pair:
            print("couldn't find overlapping pair done=%r indices=%r" % (done, indices))
            return
        i,j = pair
        print("index", i, j)
        r = np.array(scanner[i])
        #print(r)
        rr,offset = find_transformation(s, r)
        ss.append(rr)
        offsets.append(offset)
        done.append(i)
        indices.remove(i)

    # part 1: number of unique points
    seen = set(tuple(p) for s in ss for p in s)
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
        print("couldn't find valid transformation")
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
