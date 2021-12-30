def solve(file):
    lines = list(file)
    h = 0
    d = 0
    for line in lines:
        cmd, *args = line.split()
        if cmd == "forward":
            h += int(args[0])
        if cmd == "down":
            d += int(args[0])
        if cmd == "up":
            d -= int(args[0])
    print(h*d)

    h = 0
    d = 0
    a = 0
    for line in lines:
        cmd, *args = line.split()
        if cmd == "forward":
            h += int(args[0])
            d += int(args[0]) * a
        if cmd == "down":
            a += int(args[0])
        if cmd == "up":
            a -= int(args[0])
    print(h*d)

solve(open("sample"))
solve(open("input"))
