#  Сколько раз встречается в файле комбинация KTO?

with open('j5.txt', 'r') as f:
    s = f.readline()

k = 0

for i in range(0, len(s) - 1):
    if s[i] == 'K' and s[i+1] == 'T' and s[i+2] == 'O':
        k = k + 1

print(k)

# 7973
