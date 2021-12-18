with open('17.txt', 'r') as f:
    n = f.readlines()

k = 0
maxx = 0

for i in range(0, len(n) - 2):
    if int(n[i]) ** 2 + int(n[i + 1]) ** 2 == int(n[i + 2]) ** 2:
        k += 1
        a = int(n[i]) + int(n[i + 1]) + int(n[i + 2])
        if a > maxx:
            maxx = a

print(k, maxx)

# 0 0
