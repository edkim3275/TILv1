def make_set(x):
    lst = list(range(x+1))
    return lst


def find_set(x):
    if x == P[x]:
        return x
    else:
        return find_set(P[x])


def union(x, y):
    P[find_set(y)] = find_set(x)


V, E =5, 4
P = make_set(5)
union(1, 3)
print(find_set(3))
print(P)