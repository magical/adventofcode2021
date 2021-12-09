from collections import Counter
digits = []
output = []
for line in open('input'):
    w = line.split()
    digits.append(w[0:10])
    output.append(w[11:15])

#print(digits)
#print(output)

segment_counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def value(s):
    assert len(s) == 1
    return list(s)[0]

def decipher(D):
    assert sorted(len(x) for x in D) == sorted(segment_counts)

    # 1, 4, 7, 8 unique
    d1 = set([x for x in D if len(x) == 2][0])
    d4 = set([x for x in D if len(x) == 4][0])
    d7 = set([x for x in D if len(x) == 3][0])
    d8 = set([x for x in D if len(x) == 7][0])
    rest = [x for x in D if len(x) not in (2,4,3,7)]

    segs = Counter(c for x in rest for c in x)

    # 7 - 1 = a
    a = value(d7 - d1)

    # 1 == cf
    # 023569 count c < count f
    c, f = sorted(d1, key=lambda x: segs[x])
    
    # 4 - 1 = bd
    # 023569 count b < count d
    b, d = sorted(d4 - d1, key=lambda x: segs[x])

    # 8 - 47 = eg
    # count e < count g
    e, g = sorted(d8 - (d4|d7), key=lambda x: segs[x])

    #print(a,b,c,d,e,f,g, D)

    t = str.maketrans(a+b+c+d+e+f+g, 'abcdefg')
    #print(*sorted(''.join(sorted(x.translate(t))) for x in D if len(x) in (2,4,3,7)))
    T = str.maketrans('abcdefg', a+b+c+d+e+f+g)
    return [
        x.translate(T) for x in 
        ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    ]


count = 0
total = 0
for D, O in zip(digits, output):
    key = decipher(D)
    key = {frozenset(x): i for i, x in enumerate(key)}
    code = [key[frozenset(x)] for x in O]
    count += sum(code.count(n) for n in (1,4,7,8))
    total += int(''.join(map(str, code)))
    print(*code)

print(count)
print(total)




"""
# 1, 4, 7, 8 unique
#
# 7 - 1 = a
# 8 - 9 = e
# 8 - 6 = c
# 8 - 0 = d

# 8 - 1 = 6 - f

# b 

# 1 == cf
# 023569 count c < count f

# 4 - 1 = bd
# 023569 count b < count d

# 8 - 47 = e g
# count e < count g



0, 2, 3, 5, 6, 9
a  a  a  a  a  a
b        b  b  b
c  c  c        c
   d  d  d  d  d
e  e        e  
f     f  f  f  f
g  g  g  g  g  g

"""
