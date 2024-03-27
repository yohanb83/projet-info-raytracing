import couleur as c
import vecteur as v
import point as p

class Objet:
    def __init__(self,x,y,z,C,diff,spec,refl,shadow):

        if type(x)!=int and type(x)!=float:
            raise Exception("X coordinates needs to be a float or an integer")
        if type(y)!=int and type(y)!=float:
            raise Exception("Y coordinates needs to be a float or an integer")
        if type(z)!=int and type(z)!=float:
            raise Exception("Z coordinates needs to be a float or an integer")
        
        if type(C)!=c.Couleur:
            raise Exception("C component need to be a Color object")
        
        if type(diff)!=int and type(diff)!=float:
            raise Exception("Diffuse reflection factor needs to be a float or an integer")
        if type(spec)!=int and type(spec)!=float:
            raise Exception("Specular reflection factor needs to be a float or an integer")
        if type(refl)!=int and type(refl)!=float:
            raise Exception("Reflection factor needs to be a float or an integer")
        
        if type(shadow)!=bool:
            raise Exception("Shadow argument need to be of boolean type")
        
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