def creation(filein, fileout):
    parent.clear()
    rank.clear()

    fin = open(filein)
    fout = open(fileout)

    line = fin.readline().split()
    parent_size = int(line[0])
    operation_number = int(line[1])

    for i in range(parent_size):
        parent.append(i)
        rank.append(0)

    for i in range(operation_number):
        line = fin.readline().split()
        a = int(line[0])
        b = int(line[1])
        line = fout.readline()

        if get(a) != get(b):
            if line != "NO\n" and line != "NO":
                print("error in file: ", filein)
            #print("NO")
            union_sets(a, b)
        else:
            if line != "YES\n" and line != "YES":
                print("error in file: ", filein)
            #print("YES")

    print("success in file: ", filein)
    return True


def make_set(root):
    parent[root] = [root]
    rank[root] = 0


def union_sets(a, b):
    a = get(a)
    b = get(b)
    if a != b:
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


def get(x):
    if parent[x] != x:
        parent[x] = get(parent[x])

    return parent[x]


def set_tasks():
    creation("DSU_tests/1.in", "DSU_tests/1.out")
    creation("DSU_tests/2.in", "DSU_tests/2.out")
    creation("DSU_tests/3.in", "DSU_tests/3.out")
    creation("DSU_tests/4.in", "DSU_tests/4.out")

    creation("DSU_tests/2to2.in", "DSU_tests/2to2.out")
    creation("DSU_tests/2to3.in", "DSU_tests/2to3.out")
    creation("DSU_tests/2to4.in", "DSU_tests/2to4.out")
    creation("DSU_tests/2to7.in", "DSU_tests/2to7.out")
    creation("DSU_tests/2to10.in", "DSU_tests/2to10.out")
    creation("DSU_tests/2to15.in", "DSU_tests/2to15.out")
    creation("DSU_tests/2to17.in", "DSU_tests/2to17.out")
    creation("DSU_tests/2to18.in", "DSU_tests/2to18.out")
    creation("DSU_tests/2to19.in", "DSU_tests/2to19.out")
    creation("DSU_tests/2to20.in", "DSU_tests/2to20.out")


if __name__ == '__main__':
    parent = []
    rank = []

    set_tasks()
