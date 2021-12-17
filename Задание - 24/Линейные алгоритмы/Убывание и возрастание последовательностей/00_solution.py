with open('j6.txt', 'r') as f:
    s = f.readline()

k = 0
n = 1

for i in range(0, len(s)-1):
    if int(s[i]) < int(s[i+1]):
        n += 1
    else:
        if n == 5:
            k += 1
        n = 1

print(k)
