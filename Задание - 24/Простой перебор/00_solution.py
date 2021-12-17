with open('5.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s)-1):
    if s[i] == '(' and s[i+1] == ')':
        k += 1

print(k)
