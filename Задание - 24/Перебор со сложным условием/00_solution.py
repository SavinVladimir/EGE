with open('s1-2.txt', 'r') as f:
    s = f.readlines()

t_count = 10000000000000000000
index = 0

for i in range(0, len(s)):
    c = s[i].count('T')
    if c < t_count:
        t_count = c
        index = i

st = s[index]

d = dict()

for i in range(0, len(st)):
    if st[i] not in d:
        d[st[i]] = 1
    else:
        d[st[i]] += 1

print(max(d, key=d.get))

# I

i_count = 0

for i in range(0, len(s)):
    k = s[i].count('I')
    i_count += k

print(i_count)


