class UnionFind:
    def __init__(self, a):
        # Use list that will be better from an optimization stand point
        self.a = list(range(a))

    def union(self, p, q):
        """
        Union dont forget to take out the values before u send it check for it
        """
        idp = self.a[p]
        idq = self.a[q]
        for key, value in enumerate(self.a):
            if  idp == value:
                self.a[key] = idq
        return self.a

    def connection(self, p, q):
        return self.a[p] == self.a[q]

unionfind = UnionFind(10)
print(unionfind.union(1,2))
print(unionfind.union(2,8))
print(unionfind.connection(1,8))