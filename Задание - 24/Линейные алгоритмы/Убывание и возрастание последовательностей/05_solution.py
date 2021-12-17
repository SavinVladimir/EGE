with open('153.txt', 'r') as f:
    s = f.readline()

n = 1
a = []

for i in range(0, len(s) - 1):
    if s[i] == s[i+1] and s[i] == 'D':
        n += 1
    else:
        if n != 1:
            a.append(n)
        n = 1

print(min(a))
