file = open('sample')
file = open('input')
t = str.maketrans('[{(<', ']})>')
u = str.maketrans('[{(<', '2314')
score = 0
scores2 = []
no = 0
for line in file:
    no += 1
    stack = []
    for c in line.strip():
        if c in '[{(<':
            stack.append(c)
        else:
            x = stack.pop().translate(t)
            if c != x:
                print(f'line {no}: illegal {c}')
                score += {')': 3, ']': 57, '}': 1197, '>': 25137}.get(c, 0)
                break
    else:
        score2 = int(''.join(reversed(stack)).translate(u),5)
        scores2.append(score2)
        print(f"line {no}: score {score2}")

print(score)
scores2.sort()
print(scores2[len(scores2)//2])
