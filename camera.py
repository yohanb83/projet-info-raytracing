from point import Point
from droite import Droite

class Camera:
    def __init__(self, w,h,x,y,z,dir,orient,foc):
        self.width, self.height = w,h
        self.x, self.y = x,y,z
        self.direction = dir
        self.orientation = orient
        self.dist = foc

    def rayon(self, i, j):
        return Droite(Point())

    