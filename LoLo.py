
def begin():
    #size(400,600)
    fill (30,90,100)
    rect(100,100,50,50)

def middle():
     
    fill(100,100,100)
    ellipse(50,90,50,50)
    rect(mouseX,500,35,35)
    stroke(205,205,0)
    noFill()
    ellipse(mouseX,mouseY,10,10)

def laser(): 
    ship1 = triangle(30, 75, 58, 20, 86, 75) 
    shotShip1 = False 
    laserX =  mouseX 
    laserY = 75
    if mousePressed and mouseX > 400:
         line(pmouseX,pmouseY,mouseX,mouseY)
    if mouseX  or mouseY > 200:
         stroke(255,0,0)
         line(mouseX,mouseY,laserX,laserY)
    if laserX >=30 and laserY <= 75: 
        shotShip1 = True  
        fill (0) 
        ship1
    #if shotShip1 = True: 
       # fill(0)  
       # ship1
def shooter(): 
    laserX = 30 
    laserY = 75
    if laserX >=30 and laserY <= 75: 
        fill(0) 
        triangle(30, 75, 58, 20, 86, 75)
