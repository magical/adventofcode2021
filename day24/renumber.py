
import sys

def printf(fmt, *args):
    print(fmt.format(*args))

file = open("input")

var = dict(x=0, y=0, z=0, w=0, inp=0)
def read(a):
    if a.lstrip('-').isdigit():
        return 'z3.IntVal({})'.format(a)
    if a == 'inp':
        return "{}{}".format(a, var[a])
    return a
def write(a):
    var[a] += 1
    #return "{}{}".format(a, var[a])
    return a

print("import z3")
for i in range(16):
    print("inp{0} = z3.Int('inp{0}')".format(i))
# https://gist.github.com/Rufflewind/a880e03fb0d13644a1e8
print("""
def truncdiv(a,b):
    quo = a / b
    return z3.If(z3.Or(a % b == 0, a >= 0),
                 quo,
                 z3.If(b >= 0, quo + 1, quo - 1))
def truncmod(a,b):
    return a - b * truncdiv(a, b)
""")
print("x = 0")
print("y = 0")
print("z = 0")
print("w = 0")
lineno = 0
for line in file:
    lineno += 1
    cmd, *args = line.split()
    if cmd == 'inp':
        a = read('inp')
        d = write(args[0])
        printf("{} = {}", d, a)
        var['inp'] += 1
    elif cmd == 'add':
        a = read(args[0])
        b = read(args[1])
        d = write(args[0])
        printf("{} = {} + {}", d, a, b)
    elif cmd == 'mul':
        a = read(args[0])
        b = read(args[1])
        d = write(args[0])
        if b == '0':
            printf("{} = 0", d)
        else:
            printf("{} = {} * {}", d, a, b)
    elif cmd == 'div':
        a = read(args[0])
        b = read(args[1])
        d = write(args[0])
        # assume b != 0...
        printf("{} = truncdiv({}, {})", d, a, b)
    elif cmd == 'mod':
        a = read(args[0])
        b = read(args[1])
        d = write(args[0])
        # good news: mod of negative args is undefined
        #printf("{} = truncmod({}, {})", d, a, b)
        printf("{} = {} % {}", d, a, b)
    elif cmd == 'eql':
        ## TODO: does this trruncate towards 0?
        a = read(args[0])
        b = read(args[1])
        d = write(args[0])
        printf("{} = z3.If({} == {}, 1, 0)", d, a, b)
    else:
        print("{}:unknown command {}", lineno, cmd, file=sys.stderr)
print("z =", read('z'))
inps = ", ".join(["inp{0} >= 1, inp{0} <= 9".format(i) for i in range(var['inp'])])
#print("z3.solve(z == 0, {})".format(inps))
print("s = z3.Solver()")
#print("s = z3.Optimize()")
for i in range(var['inp']):
    print("s.add(inp{0} >= 1, inp{0} <= 9)".format(i))
#print("s.minimiz
print("s.add(z == 0)")
print("print(s.check())")
#print("print(s.model())")
print("inputs = [{}]".format(",".join("inp{}".format(i) for i in range(var['inp']))))
