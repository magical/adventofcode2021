def solve(file):
    bits = [x.strip() for x in file]
    gamma = ""
    epsilon = ""
    for i in range(len(bits[0])):
        b = "".join(x[i] for x in bits)
        gamma += "01"[b.count("1") > len(bits)//2]
        epsilon += "01"[b.count("1") < len(bits)//2]
    print(int(gamma,2) * int(epsilon,2))

solve(open("sample"))
solve(open("input"))

def part2(file):
    bits = [x.strip() for x in file]
    oxygen = bits
    co2 = bits
    for i in range(len(bits[0])):
        if len(oxygen) > 1:
            b = "".join(x[i] for x in oxygen)
            crit = "01"[b.count("0") <= b.count("1")]
            oxygen = [x for x in oxygen if x[i] == crit]
            crit0 = crit

        if len(co2) > 1:
            b = "".join(x[i] for x in co2)
            crit = "01"[b.count("0") > b.count("1")]
            co2 = [x for x in co2 if x[i] == crit]

    assert len(oxygen) == len(co2) == 1
    print(int(oxygen[0],2) * int(co2[0],2))

part2(open("sample"))
part2(open("input"))
