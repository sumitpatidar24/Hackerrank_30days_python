class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        
        a.sort()
        b=a[len(a)-1]-a[0]
                
                
        
        self.maximumDifference=b


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
