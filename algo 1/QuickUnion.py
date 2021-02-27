class UnionUnion:
    def __init__(self, a):
        # Use list that will be better from an optimization stand point
        self.array = list(range(a))

    def union(self, p, q):
        self.array[p] = self.array[q]
        return self.array
    
    def findroot(self, val):
        while (val != self.array[val]):
            print(self.array[val], val)
            val = self.array[val]
        return val
    
    def connection(self, p, q):
        aa = self.findroot(p) 
        bb = self.findroot(q) 
        return aa == bb

class UnionUnionWeighted:
    def __init__(self, a):
        # Use list that will be better from an optimization stand point
        self.array = list(range(a))
        self.weight = list(range(a))

    # only change for weighted quick union including the new array
    def union(self, p, q):
        """
        Check the weight of the graph before u add the q to p
        """
        if self.findroot(p) == self.findroot(q):
            return self.array
        elif self.weight[p] < self.weight[q]:
            self.array[p] = self.findroot(q)
            self.weight[q] += self.weight[p]
        elif self.weight[p] > self.weight[q]:
            self.array[q] = self.findroot(p)
            self.weight[p] += self.weight[q]
    
    def findroot(self, val):
        while (val != self.array[val]):
            print(self.array[val], val)
            val = self.array[val]
        return val
    
    def connection(self, p, q):
        aa = self.findroot(p) 
        bb = self.findroot(q) 
        return aa == bb


t = UnionUnionWeighted(8)
print(t.union(5,7))
print(t.union(4,5))
print(t.connection(4,7))