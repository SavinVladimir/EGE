# SOCKCOS

with open('j5.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s) - 1):
    if s[i] == 'S' and s[i + 1] == 'O' and s[i + 2] == 'C' and s[i + 3] == 'K' and s[i+4] == 'C' and s[i + 5] == 'O' and \
            s[i+6] == 'S':
        k = k + 1

print(k)

# 15
