import couleur as c
import objet as o

class Sphere(o.Objet):
    def __init__(self,x,y,z,C,diff,spec,refl,shadow,r):
        o.Objet.__init__(self,x,y,z,C,diff,spec,refl,shadow)
        self.radius = r
