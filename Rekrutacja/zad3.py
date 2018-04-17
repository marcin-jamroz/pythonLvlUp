triangle = list()

with open("triangle.txt", "r") as file:    
    for line in file:
        triangle.append(line.strip().split(" "))


def path(cen, depth, tr):
    if(depth == len(tr) - 1):
        war = tr[depth][cen]
        return war

    l_len = int(tr[depth][cen]) + int(path(cen, depth + 1, tr))
    r_len = int(tr[depth][cen]) + int(path(cen + 1, depth + 1, tr))

    if l_len > r_len:
        return l_len
    else:
        return r_len


length = path(0, 0, triangle)
print(length)