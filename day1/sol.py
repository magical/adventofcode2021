t = -1
prev = -100
for line in open("input"):
    n = int(line)
    if n > prev:
        t += 1
    prev = n
print(t)
