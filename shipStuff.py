xCoord = 550 
yCoord = 550 
xSpeed = 10
ySpeed = 10
ellipseSize = 30 

def flyingShip(): 


    global xCoord, yCoord,y, xSpeed, ySpeed, ellipseSize 
    leftBoundary = ellipseSize / 2 
    rightBoundary = 400 - ellipseSize / 2 
    topBoundary = 540 - ellipseSize / 2  
    bottomBoundary = 600 - ellipseSize /2 
    xCoord += xSpeed 
    yCoord += ySpeed 

    if mouseX >= rightBoundary or mouseX<= leftBoundary: 
        xSpeed = -xSpeed  
    if yCoord >= bottomBoundary or yCoord<= topBoundary: 
        ySpeed = -ySpeed
    fill(255, 255, 255) 
    shipY = mouseY        #top boundary for ship
    if shipY < 420: 
        shipY =  420
    #Player Ship
    noStroke()
    fill(255,0,0)
    rect(mouseX,500,35,35)
    fill(255)
    triangle(mouseX-3, 535, mouseX+17, 480, mouseX+38, 535)
    fill(50,120,255)
    ellipse(mouseX+17, 513, 13, 33)
    
    #ellipse(mouseX, shipY, ellipseSize, ellipseSize) 
    
    
