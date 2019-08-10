class rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return(self.l*self.w)

l=int(input("l="))
w=int(input("w="))
r=rect(l,w)
print('area=',r.area())
