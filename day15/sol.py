from collections import namedtuple

def load(f):
    lines = [x.strip() for x in f if x.strip()]
    height = len(lines)
    width = len(lines[0])
    values = [list(map(int, x)) for x in lines]
    return Graph(width, height, values)

class Graph(namedtuple('Graph', "width, height, values")):
    def risk(G, pos):
        x,y = pos
        if not 0 <= x < G.width:
            return 1000
        if not 0 <= y < G.height:
            return 1000
        return G.values[y][x]
    def neighbors(G, pos):
        x, y = pos
        return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def bestpath(G, start=(0,0), end=None):
    if end == None:
        end = (G.width-1, G.height-1)
    queue = [(0,start)] # risk, pos
    seen = set()
    while queue:
        queue.sort()
        c, here = queue.pop(0)
        if here in seen:
            continue
        #print(c, here)
        if here == end:
            return c
        seen.add(here)
        for n in G.neighbors(here):
            if n not in seen:
                r = G.risk(n)
                #print(c, r, here, n)
                if r < 1000:
                    queue.append((c+r, n))

print(bestpath(load(open('sample'))))
print(bestpath(load(open('input'))))
