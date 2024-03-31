import couleur as c
import vecteur as v
import point as p

class Objet:
    def __init__(self,x,y,z,C,diff,spec,refl,shadow):        
        self.x, self.y, self.z = x,y,z
        self.color = C
        self.diffuse = diff
        self.specular = spec
        self.reflexion = refl
        self.shadow = shadow

    def intersection(self, d):
        return 
    
    def normal(self, p):
        return v.Vecteur(self.x, self.y, self.z, p.x, p.y, p.z)