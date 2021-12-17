with open('5.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s)):
    if s[i] == '(':
        k += 1
    if k == 100:
        print(i+1)
