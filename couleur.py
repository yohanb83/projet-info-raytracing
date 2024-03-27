class Couleur:
    def __init__(self,r,v,b):

        if type(r)!=int and type(r)!=float:
            raise Exception("R value for color needs to be of integer or float type")
        elif type(v)!=int and type(v)!=float:
            raise Exception("V value for color needs to be of integer or float type")
        elif type(b)!=int and type(b)!=float:
            raise Exception("B value for color needs to be of integer or float type")
        
        if r<0 or r>1:
            raise Exception("R value for color needs to be between 0 and 1")
        elif v<0 or v>1:
            raise Exception("V value for color needs to be between 0 and 1")
        elif b<0 or b>1:
            raise Exception("B value for color needs to be between 0 and 1")
        
        self.r, self.v, self.b = r,v,b

    def __add__(self, C):
        # A voir normalisation
        return Couleur(self.r+C.r, self.v+C.v, self.b+C.b)
    
    def __mul__(self, i):
        # A voir normalisation
        return Couleur(self.r*i, self.v*i, self.b*i)
    
c = Couleur(1,1,1)
print(type(c)==Couleur)
    
