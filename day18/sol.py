class Pair:
    def __init__(self, a=None, b=None, value=None):
        self.a = a
        self.b = b
        self.value = value
    def ispair(self):
        return self.value is None

    @classmethod
    def fromlist(cls, l):
        if isinstance(l,list):
            return cls(cls.fromlist(l[0]), cls.fromlist(l[1]))
        else:
            return cls(value=l)

    def __str__(self):
        if self.ispair():
            return "[" + str(self.a) + "," + str(self.b) + "]"
        else:
            return str(self.value)

def add(a,b):
    p = Pair(a,b)
    reduce(p)
    return p

def link(top):
    """go through the tree and assign left,right links to each leaf node"""
    def recurse(p):
        if p.ispair():
            yield from recurse(p.a)
            yield from recurse(p.b)
        else:
            yield p

    prev = None
    for p in recurse(top):
        p.left = prev
        if p.left is not None:
            p.left.right = p
        prev = p
    p.right = None

def explode(top):
    link(top)
    def recurse(p, depth):
        if p.ispair():
            if depth >= 4 and not p.a.ispair() and not p.b.ispair():
                return p
            else:
                ret = recurse(p.a, depth+1)
                if ret == None:
                    ret = recurse(p.b, depth+1)
                return ret

    # find the leftmost pair of numbers at depth >= 4 and the numbers to either side of it
    p = recurse(top,0)
    if p is None:
        return False
    else:
        left = p.a.left
        right = p.b.right
        #print("explode", left, p, right)
        if left:
            assert not left.ispair()
        if right:
            assert not right.ispair()
        assert not p.a.ispair()
        assert not p.b.ispair()
        if left:
            left.value += p.a.value
        if right:
            right.value += p.b.value
        p.a = None
        p.b = None
        p.value = 0
        return True

def split(top):
    def recurse(p):
        if p.ispair():
            ret = recurse(p.a)
            if ret == None:
                ret = recurse(p.b)
            return ret
        else:
            if p.value >= 10:
                return p

    p = recurse(top)
    if p is None:
        return False

    # To split a regular number, replace it with a pair; the left element of
    # the pair should be the regular number divided by two and rounded down,
    # while the right element of the pair should be the regular number divided
    # by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6],
    # 12 becomes [6,6], and so on.
    #print("split", p)
    p.a = Pair(value=p.value//2)
    p.b = Pair(value=(p.value+1)//2)
    p.value = None
    return True

def reduce(top):
    while True:
        if explode(top):
            continue
        if split(top):
            continue
        break

def magnitude(p):
    if p.ispair():
        return 3*magnitude(p.a) + 2*magnitude(p.b)
    return p.value

def main():
    def test(l):
        p = Pair.fromlist(l)
        before = str(p)
        reduce(p)
        print(before, "->", p, " ("+str(magnitude(p))+")")
    test( [[[[[9,8],1],2],3],4] )
    test( [7,[6,[5,[4,[3,2]]]]] )
    test( [[6,[5,[4,[3,2]]]],1] )
    test( [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] )
    test( [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] )

    test( [ [[[[4,3],4],4],[7,[[8,4],9]]] , [1,1] ] )

    p = None
    for line in open("input"):
        l = eval(line.strip()) # don't try this at home
        if p is None:
            p = Pair.fromlist(l)
        else:
            p = add(p, Pair.fromlist(l))
    print(p)
    print(magnitude(p))

    numbers = []
    for line in open("input"):
        numbers.append(eval(line.strip()))
    def product():
        for a in numbers:
            for b in numbers:
                if a == b:
                    continue
                n = magnitude(add(Pair.fromlist(a), Pair.fromlist(b)))
                yield n
    print(max(product()))

main()
    
