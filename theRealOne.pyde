from themBoys import * 
from shipStuff import *
from Ships import *
from LoLo import*


def setup(): 
    size(400, 600) 
def draw():
    background(0, 0, 0)
    #flyingShip()
    ships()
    themBoys() 
    #middle()
def mouseClicked():
    laser()
