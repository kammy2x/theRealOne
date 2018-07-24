from themBoys import * 
from shipStuff import *
from LoLo import*

def setup(): 
    size(400, 600) 
def draw():
    background(0, 0, 0)
    themBoys() 
    flyingShip()
    middle()
def mouseClicked():
    laser()
