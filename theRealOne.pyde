from themBoys import * 
from shipStuff import *
from Ships import *
from LoLo import*


def setup(): 
    size(400, 600) 
def draw():
    background(0, 0, 0)
    img = loadImage("starGround2.png")
    image(img, 0, 0)
    ships()
    themBoys() 
    flyingShip() 
    #shooter()
    #middle()
def mouseClicked():
    laser() 
    
    
