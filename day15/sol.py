from collections import namedtuple
from heapq import heappush, heappop

def load(f):
    lines = [x.strip() for x in f if x.strip()]
    height = len(lines)
    width = len(lines[0])
    values = [list(map(int, x)) for x in lines]
    return Graph(width, height, values)

MAX = 100000

class Graph(namedtuple('Graph', "width, height, values")):
    def risk(G, pos):
        x,y = pos
        bonus = 0
        if not 0 <= x < 5*G.width:
            return MAX
        if not 0 <= y < 5*G.height:
            return MAX
        bonus = y//G.height + x//G.width
        v = G.values[y%G.height][x%G.width]
        return (v+bonus-1)%9 + 1
    def neighbors(G, pos):
        x, y = pos
        return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def bestpath(G, start=(0,0), end=None):
    if end == None:
        end = (G.width-1, G.height-1)
    queue = [(distance(start,end),start)] # reduced risk, pos
    seen = set()
    while queue:
        c, here = heappop(queue)
        if here in seen:
            continue
        #print(c, here)
        if here == end:
            return c
        seen.add(here)
        k = distance(here,end)
        for n in G.neighbors(here):
            if n not in seen:
                r = G.risk(n)
                if r < MAX:
                    h = distance(n, end)
                    heappush(queue, (c+r+h-k, n))

def distance(a,b):
    """manhattan distance between points a and b"""
    return abs(a[0]-b[0])+abs(a[1]-b[1])

sample = load(open('sample'))
input = load(open('input'))
print(bestpath(sample))
print(bestpath(input))
#for y in range(sample.height*5):
#    print(''.join(str(sample.risk((x,y))) for x in range(sample.width*5)))
print(bestpath(sample, end=(sample.width*5-1, sample.height*5-1)))
print(bestpath(input, end=(input.width*5-1, input.height*5-1)))
