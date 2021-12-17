with open('5.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s)):
    if s[i] == '(' and s[i+1] == ')':
        k += 1
    if k == 10000:
        print(i + 1)
        break


