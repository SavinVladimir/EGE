with open('j8.txt', 'r') as f:
    s = f.readline()

maxx = 0
k = 1

for i in range(1, len(s)):
    if int(s[i-1]) + int(s[i]) >= 10:
        k += 1
        if k > maxx:
            maxx = k
    else:
        k = 1

print(maxx)
