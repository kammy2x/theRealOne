laserY = 75 
shotShip1 = False 
shotShip2 = False
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
    global laserY, shotShip1
    ship1 = triangle(30, 75, 58, 20, 86, 75) 
    if mousePressed and mouseX > 400:
         line(pmouseX,pmouseY,mouseX,mouseY)
    if mouseX  or mouseY > 200:
         stroke(255,0,0)
         line(mouseX,mouseY,mouseX,laserY)
         
def shotShips():
    global laserY, shotShip1 
    
    if mousePressed and mouseX >=30 and mouseX <=86: #Conditional to make ships disappear
        shotShip1 = True  
        fill (0) 
        triangle(30, 75, 58, 20, 86, 75)
    if shotShip1 == True:                            #Conditional to keep the ship "gone"
        fill(0) 
        triangle(30, 75, 58, 20, 86, 75) 

        
#def shooter(): 
    #laserX = 30 
    #laserY = 75
    #if laserX >=30 and laserY <= 75: 
        #fill(0) 
        #triangle(30, 75, 58, 20, 86, 75)
