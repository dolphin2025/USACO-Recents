import itertools

for testcase in range(int(input())):
    n = int(input())
    inp, triples = [int(i) for i in input().split()] + [-1] * (7 - n), set()
    for ar in set(itertools.permutations(inp)):
        a, b, c, ab, bc, ac, abc = ar

        if ab != -1 and b != -1: a = ab - b
        elif ac != -1 and c != -1: a = ac - c
        elif abc != -1 and bc != -1: a = abc - bc
        if ab != -1 and a != -1: b = ab - a
        elif bc != -1 and c != -1: b = bc - c
        elif abc != -1 and ac != -1: b = abc - ac
        if abc != -1 and ab != -1: c = abc - ab
        elif ac != -1 and a != -1: c = ac - a
        elif bc != -1 and b != -1: c = bc - b

        if all([a,b,c,a+b,b+c,a+c,a+b+c][i]==ar[i] or ar[i]==-1 for i in range(7)) and 1<=a<=b<=c: triples.add((a,b,c))
    print(len(triples))
