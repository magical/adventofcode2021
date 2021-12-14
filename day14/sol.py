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

def expand_pairs(pairs, rules):
    result = Counter()
    for p, count in pairs.items():
        if p in rules:
            r = rules[p]
            result[p[0] + r] += count
            result[r + p[1]] += count
        else:
            result[p] += count
    return result

def score(seq):
    h = Counter(seq).most_common()
    top, bottom = h[0][1], h[-1][1]
    return top - bottom

def score_after(init, n):
    seq, rules = init
    q = Counter(a+b for a, b in zip(seq, seq[1:]))
    for _ in range(n):
        q = expand_pairs(q, rules)
        #print(q)
    counts = Counter()
    for p, count in q.items():
        counts[p[0]] += count
        counts[p[1]] += count
    # double-counts everything except the first and last character
    counts[seq[0]] += 1
    counts[seq[-1]] += 1
    h = counts.most_common()
    return h[0][1]//2 - h[-1][1]//2

print(expand(*input))

sample = parse(open("sample"))
q = sample[0]
for _ in range(5):
    q = expand(q, sample[1])
    print(q)

print(score_after(sample, 10))
print(score_after(input, 10))
print(score_after(sample, 40))
print(score_after(input, 40))
