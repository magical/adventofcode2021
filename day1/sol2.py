data = [int(n) for n in open('input')]
avg = [a+b+c for a,b,c in zip(data, data[1:], data[2:])]

t = -1
prev = -100
for n in avg:
    if n > prev:
        t += 1
    prev = n
print(t)
