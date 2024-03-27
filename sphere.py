import couleur as c
import objet as o

class Sphere(o.Objet):
    def __init__(self,x,y,z,C,diff,spec,refl,shadow,r):
        o.Objet.__init__(self,x,y,z,C,diff,spec,refl,shadow)
        self.radius = r




RED = c.Couleur(1,0,0)
s = Sphere(0,0,0,RED,1,1,1,False,10)