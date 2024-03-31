class Couleur:
    def __init__(self,r,v,b):
        self.r, self.v, self.b = r,v,b

    def __add__(self, C):
        # A voir normalisation
        return Couleur(self.r+C.r, self.v+C.v, self.b+C.b)
    
    def __mul__(self, i):
        # A voir normalisation
        return Couleur(self.r*i, self.v*i, self.b*i)
    
    def rvb(self):
        return (self.r, self.v, self.b)