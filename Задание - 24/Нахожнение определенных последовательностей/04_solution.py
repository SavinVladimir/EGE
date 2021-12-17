# Определите количество палиндромов длиной 5 символов.

with open('j9.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(4, len(s)):
    if s[i-4] == s[i] and s[i-3] == s[i-1]:
        k += 1

print(k)
