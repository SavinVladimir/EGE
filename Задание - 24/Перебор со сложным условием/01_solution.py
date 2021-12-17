with open('s1-2.txt', 'r') as f:
    s = f.readlines()

n_count = 0
index = 0

for i in range(0, len(s)):
    c = s[i].count('N')
    if c > n_count:
        n_count = c
        index = i

st = s[index]

d = dict()

for i in range(0, len(st)):
    if st[i] not in d:
        d[st[i]] = 1
    else:
        d[st[i]] += 1

print(d)

# s

s_count = 0

for i in range(0, len(s)):
    k = s[i].count('S')
    s_count += k

print(s_count)


