with open('s2.txt', 'r') as f:
    s = f.readline()

d = dict()

for i in range(1, len(s)-1):
    if s[i-1] == 'A' and s[i] != 'A':
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1

print(d)

