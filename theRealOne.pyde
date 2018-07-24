from themBoys import * 
from shipStuff import *
from Ships import *
from LoLo import*


def setup(): 
    size(400, 600) 
def draw():

    flyingShip()
    ships()
    themBoys()
    background(0, 0, 0)
    themBoys() 
    flyingShip()
    middle()
def mouseClicked():
    laser()
    
