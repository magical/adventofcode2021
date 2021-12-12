def load(f):
    V = set()
    E = {}
    for line in f:
        a, b = line.strip().split('-')
        V.add(a)
        V.add(b)
        if b != 'start':
            E.setdefault(a, []).append(b)
        if a != 'start':
            E.setdefault(b, []).append(a)
    return V, E

def paths(G, revisits=0):
    V, E = G
    path = []
    def dfs(here, revisits):
        if here == 'end':
            return 1
        if here.islower() and here in path:
            if revisits > 0:
                revisits -= 1
            else:
                return 0
        path.append(here)
        ret = 0
        for n in E[here]:
            if not n.islower() or revisits > 0 or n not in path:
                ret += dfs(n, revisits)
        path.pop()
        return ret
    return dfs('start', revisits)

print(paths(load(open('sample'))))
print(paths(load(open('input'))))
print(paths(load(open('input')), revisits=1))
