f = open('s1 (1).txt', 'r')
s = f.readline()

a = 0

while s:
    k = 0
    for i in range(1, len(s) - 1):
        if s[i-1] == 'A' and s[i+1] == 'B':
            k = k + 1

    if k > 5:
        a = a + 1

    s = f.readline()

print(a)

f.close()
