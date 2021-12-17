with open('5.txt', 'r') as f:
    s = f.readline()

maxx = 0
n = 1
st = s[0]
sm = ''

for i in range(0, len(s)-1):
    if s[i] > s[i+1]:
        n += 1
        st += s[i+1]
        if n > maxx:
            maxx = n
            sm = st
    else:
        n = 1
        st = s[i+1]

print(sm, maxx)
