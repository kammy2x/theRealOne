from themBoys import * 
from shipStuff import *
from Ships import *
from LoLo import*
sumSumn = True
score = 0


def setup(): 
    size(400, 600)
def draw():
    global sumSumn, score , answer
    
    if sumSumn == True:
        g = "Start"
        p = loadImage("galaxyGrounds.jpg")
        l = "Spaceland Adventure"
        image(p, 0, 0)
        loadFont("CopperplateGothic-Bold-48.vlw")
        fill(255, 90, 255) #find perfect color for words
        textSize(32)
        text(l, 30, 100)
        fill(random(255), random(255), random(255)) #not sure I want this to be flashing, might need to find definite color.
        rect(100, 300, 200, 100)
        loadFont("PermanentMarker-48.vlw")
        textSize(32)
        fill(0)
        text(g, 160, 360)
    if mousePressed and mouseX >= 100 and mouseX <= 300 and mouseY >= 300 and mouseY <= 400:
            sumSumn = False
    elif sumSumn == False:
        
        background(0, 0, 0)
        img = loadImage("starGround2.png")
        image(img, 0, 0)
        themBoys()
        #ships()
        flyingShip() 
        shotShips()
        #middle()
def mouseClicked():
    laser() 
