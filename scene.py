from PIL import Image
import numpy as np

from camera import Camera
from couleur import Couleur
from objet import Objet
from sphere import Sphere


class Scene:
    def __init__(self, camera, listObjets = None, listLights = None, ambient = 0, Im = None):

        self.camera = camera
        if listObjets == None:
            self.listObjets = []
        else:
            self.listObjets = listObjets
        if listLights == None:
            self.listLights = []
        else:
            self.listLights = listLights
        self.ambient = ambient
        self.image = Im



    def show_scene(self):
        return 
    

if __name__ == "__main__":
    print("Execution du programme principal scene.py")

    IMAGE_SIZE_X, IMAGE_SIZE_Y = 500, 500
    YELLOW = Couleur(0,255,255)
    imageMatrix = np.zeros((IMAGE_SIZE_X, IMAGE_SIZE_Y, 3), dtype=np.uint8)
    imageMatrix[:] = (0,0,0)

    img = Image.fromarray(imageMatrix) 
    img.show()

    mainCamera = Camera(20,20, 0,0, 0,0, 5)

    scene = Scene(mainCamera)

    sphere = Sphere(0,0,0, YELLOW, 0,0,0,0,10)
    scene.listObjets += [sphere]

    





    #mainCamera = Camera()

