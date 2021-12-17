with open('j5.txt', 'r') as f:
    line = f.readline()

print(line.count("TOK") - line.count("TOTOK"))

# 7758
