import math as m

class Vecteur:
    def __init__(self, x0, y0, z0, x1, y1, z1):

        if type(x0)!=int and type(x0)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        elif type(y0)!=int and type(y0)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        elif type(z0)!=int and type(z0)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        elif type(x1)!=int and type(x1)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        elif type(y1)!=int and type(y1)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        elif type(z1)!=int and type(z1)!=float:
            raise Exception("x0 value for vector needs to be of integer or float type")
        
        if x0<0 and x0>1:
            raise Exception("x0 value needs to be between 0 and 1")
        if y0<0 and y0>1:
            raise Exception("y0 value needs to be between 0 and 1")
        if z0<0 and z0>1:
            raise Exception("z0 value needs to be between 0 and 1")
        if x1<0 and x1>1:
            raise Exception("x1 value needs to be between 0 and 1")
        if y1<0 and y1>1:
            raise Exception("y1 value needs to be between 0 and 1")
        if z1<0 and z1>1:
            raise Exception("z1 value needs to be between 0 and 1")

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

A = Vecteur(0,0,0, 1,1,1)
B = A.normalize()
print(B.origine, B.extremite, B.lenght())


        