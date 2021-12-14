import itertools
from collections import Counter
def parse(f):
    seq = f.readline().strip()
    rules = []
    for line in f:
        if line.strip():
            rules.append(tuple(line.strip().split(" -> ")))
    return seq, dict(rules)

input = parse(open("input"))
print(input[0], next(iter(input[1].items())), len(input[1]))

def expand(seq, rules):
    pairs = zip(seq, seq[1:])
    result = []
    for i, c in enumerate(seq):
        result.append(c)
        p = seq[i:i+2]
        if p in rules:
            result.append(rules[p])
    return ''.join(result)

def score(seq):
    h = Counter(seq).most_common()
    top, bottom = h[0][1], h[-1][1]
    return top - bottom

print(expand(*input))

sample = parse(open("sample"))
q = sample[0]
for _ in range(5):
    q = expand(q, sample[1])
    print(q)

q = sample[0]
for _ in range(10):
    q = expand(q, sample[1])
print(score(q))

q = input[0]
for _ in range(40):
    q = expand(q, input[1])
print(score(q))
