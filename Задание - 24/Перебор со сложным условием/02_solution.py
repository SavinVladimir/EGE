with open('j9.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s)//2):
    if s[i] == s[len(s)-i-1]:
        k += 1

print(k)
