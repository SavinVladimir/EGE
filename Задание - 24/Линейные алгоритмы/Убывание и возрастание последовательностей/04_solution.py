with open('5.txt', 'r') as f:
    s = f.readline()

n = 1
maxx = 0
a = 0

for i in range(0, len(s)-1):
    if s[i] < s[i+1]:
        n += 1
        if n > maxx:
            maxx = n
            a = i
    else:
        n = 1

print(a-maxx + 3)
