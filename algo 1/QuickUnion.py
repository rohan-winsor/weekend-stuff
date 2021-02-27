class UnionUnion:
    def __init__(self, a):
        # Use list that will be better from an optimization stand point
        self.a = list(range(a))

    def union(self, p, q):
        """
        Union dont forget to take out the values before u send it check for it
        """
        self.a[p] = self.a[q]
        return self.a
    
    def findroot(self, val):
        while (val != self.a[val]):
            print(self.a[val], val)
            val = self.a[val]
        return val
    
    def connection(self, p, q):
        aa = self.findroot(p) 
        bb = self.findroot(q) 
        return aa == bb


t = UnionUnion(8)
print(t.union(5,7))
print(t.union(4,5))
print(t.connection(4,7))