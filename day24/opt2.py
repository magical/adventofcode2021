from output import z3, s, inputs

for inp in inputs:
    m = s.model()
    print(m)
    n = m[inp].as_long()
    while n > 1:
        s.push()
        s.add(inp < n)
        if not s.check() == z3.sat:
            s.pop()
            break
        print(".")
        n -= 1
    print(n)
    s.add(inp == n)
    s.check()
m = s.model()
print(m)
print("".join(str(m[inp]) for inp in inputs))
