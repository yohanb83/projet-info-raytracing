import math as m

class Vecteur:
    def __init__(self, x0, y0, z0, x1, y1, z1):
        self.origine = (x0,y0,z0)
        self.extremite = (x1,y1,z1)
        self.dx = self.extremite[0]-self.origine[0]
        self.dy = self.extremite[1]-self.origine[1]
        self.dz = self.extremite[2]-self.origine[2]

    def __add__(self, V):
        return Vecteur(self.origine[0], self.origine[1], self.origine[2],
                       V.extremite[0], V.extremite[1], V.extremite[2])
    
    def __sub__(self, V):
        return Vecteur(self.origine[0], self.origine[1], self.origine[2],
                       V.origine[0]+V.dx, V.origine[1]+V.dy, V.origine[2]+V.dz)
    
    def __mul__(self, scal):
        return Vecteur(self.origine[0], self.origine[1], self.origine[2],
                       self.origine[0]+self.dx*scal, self.origine[1]+self.dy*scal, self.origine[2]+self.dz*scal)
    
    def dotprod(self, V):
        return self.dx*V.dx + self.dy*V.dy + self.dz*V.dz
    
    def vectprod(self, V):
        dx = self.dy*V.dz-self.dz-V.dy
        dy = self.dz*V.dx-self.dx-V.dz
        dz = self.dx*V.dy-self.dy-V.dx
        return Vecteur(0,0,0, dx,dy,dz)
    
    def normalize(self):
        n = self.lenght()
        return Vecteur(0,0,0, self.dx/n, self.dy/n, self.dz/n)
    
    def lenght(self):
        return m.sqrt(self.dx**2+self.dy**2+self.dz**2)