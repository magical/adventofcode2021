import z3
inp0 = z3.Int('inp0')
inp1 = z3.Int('inp1')
inp2 = z3.Int('inp2')
inp3 = z3.Int('inp3')
inp4 = z3.Int('inp4')
inp5 = z3.Int('inp5')
inp6 = z3.Int('inp6')
inp7 = z3.Int('inp7')
inp8 = z3.Int('inp8')
inp9 = z3.Int('inp9')
inp10 = z3.Int('inp10')
inp11 = z3.Int('inp11')
inp12 = z3.Int('inp12')
inp13 = z3.Int('inp13')
inp14 = z3.Int('inp14')
inp15 = z3.Int('inp15')

def truncdiv(a,b):
    quo = a / b
    return z3.If(z3.Or(a % b == 0, a >= 0),
                 quo,
                 z3.If(b >= 0, quo + 1, quo - 1))
def truncmod(a,b):
    return a - b * truncdiv(a, b)

x = 0
y = 0
z = 0
w = 0
w = inp0
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(14)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(16)
y = y * x
z = z + y
w = inp1
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(11)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(3)
y = y * x
z = z + y
w = inp2
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(12)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(2)
y = y * x
z = z + y
w = inp3
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(11)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(7)
y = y * x
z = z + y
w = inp4
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-10)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(13)
y = y * x
z = z + y
w = inp5
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(15)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(6)
y = y * x
z = z + y
w = inp6
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-14)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(10)
y = y * x
z = z + y
w = inp7
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(10)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(11)
y = y * x
z = z + y
w = inp8
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-4)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(6)
y = y * x
z = z + y
w = inp9
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-3)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(5)
y = y * x
z = z + y
w = inp10
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(1))
x = x + z3.IntVal(13)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(11)
y = y * x
z = z + y
w = inp11
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-3)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(4)
y = y * x
z = z + y
w = inp12
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-9)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(4)
y = y * x
z = z + y
w = inp13
x = x * z3.IntVal(0)
x = x + z
x = x % z3.IntVal(26)
z = truncdiv(z, z3.IntVal(26))
x = x + z3.IntVal(-12)
x = z3.If(x == w, 1, 0)
x = z3.If(x == z3.IntVal(0), 1, 0)
y = y * z3.IntVal(0)
y = y + z3.IntVal(25)
y = y * x
y = y + z3.IntVal(1)
z = z * y
y = y * z3.IntVal(0)
y = y + w
y = y + z3.IntVal(6)
y = y * x
z = z + y
z = z
s = z3.Solver()
s.add(inp0 >= 1, inp0 <= 9)
s.add(inp1 >= 1, inp1 <= 9)
s.add(inp2 >= 1, inp2 <= 9)
s.add(inp3 >= 1, inp3 <= 9)
s.add(inp4 >= 1, inp4 <= 9)
s.add(inp5 >= 1, inp5 <= 9)
s.add(inp6 >= 1, inp6 <= 9)
s.add(inp7 >= 1, inp7 <= 9)
s.add(inp8 >= 1, inp8 <= 9)
s.add(inp9 >= 1, inp9 <= 9)
s.add(inp10 >= 1, inp10 <= 9)
s.add(inp11 >= 1, inp11 <= 9)
s.add(inp12 >= 1, inp12 <= 9)
s.add(inp13 >= 1, inp13 <= 9)
s.add(z == 0)
print(s.check())
inputs = [inp0,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13]
