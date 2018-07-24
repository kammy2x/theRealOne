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
    ellipse(mouseX, shipY, ellipseSize, ellipseSize)
