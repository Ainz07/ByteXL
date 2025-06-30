n = int(input())
strings = [input().strip() for _ in range(n)]
data = [(s, s.count('s'), s.count('h')) for s in strings]
data.sort(key=lambda x: (x[1] / (x[2] + 1e-9)), reverse=True)
result = ''.join(d[0] for d in data)

s_count = 0
noise = 0
for c in result:
    if c == 's':
        s_count += 1
    else:
        noise += s_count

print(noise)