# Quick find algorithm from Coursera course

class QuickUnion(object):
    def __init__(self, size):
        self.d = list(range(size))

    def root(self, num):
        'find root of an index'
        indx = num
        while indx != self.d[indx]:
            indx = self.d[indx]
        return indx

    def connected(self, p, q):
        'find if two elements are connected'
        return self.root(p) == self.root(q)

    def union(self, p, q):
        'merge two elements by equaling their values'
        self.d[self.root(p)] = self.root(q)

def test1():
    instancia = QuickUnion(10)
    instancia.union(4,3)
    instancia.union(3,8)
    instancia.union(6,5)
    instancia.union(9,4)
    instancia.union(2,1)
    assert instancia.connected(8,9) == True, "Test failed"
    assert instancia.connected(5,4) == False, "Test failed"
    assert instancia.connected(4,3) == True, "Test failed"
    #assert instancia.root(3) == 3, "Test failed"
    instancia.union(5,0)
    instancia.union(7,2)
    instancia.union(6,1)
    instancia.union(7,3)
    print("Tests passed")
    print(instancia.d)

test1()
