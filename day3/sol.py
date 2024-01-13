f = open("input.txt")

mat = []
for l in f.readlines():
    if len(l) > 0:
        mat.append(list(l[0:len(l)-1]))

print(mat)
