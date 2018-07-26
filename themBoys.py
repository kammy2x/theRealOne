import LoLo
xSpeed = 2 
xSpeed2 = 2 
xSpeed3 = 2 
xSpeed4 = 2  
xSpeed5 = 2 
xSpeed6 = 2 
xSpeed7 = 2
xCoord = 58 
yCoord = 50 
xCoord2 = 148 
xCoord3 = 238 
xCoord4 = 328
yCoord2 = 135 
xCoord5 = 108 
xCoord6 = 198 
xCoord7 = 298

def themBoys(): 
    global xCoord, yCoord, xCoord2, xCoord3, xCoord4, xCoord5, xCoord6, xCoord7, xSpeed, xSpeed2, xSpeed3, xSpeed4, xSpeed5, xSpeed6, xSpeed7, shotShip1, shotShip2, shotShip3, shotShip4, shotShip5, shotShip6, shotShip7   
    if LoLo.shotShip1 == False:
        fill(155)
        triangle(xCoord -28,yCoord+25, xCoord, 20, xCoord +28, 75) #1stship
        fill(185,0,255) 
        ellipse(xCoord,yCoord,15,40) 
        xCoord += xSpeed 
        if xCoord +28 >= 100 or xCoord - 28<= 20: 
            xSpeed = -xSpeed 
    if LoLo.shotShip2 == False:
        fill(155)
        triangle(xCoord2 -28, yCoord+25, xCoord2, 20, xCoord2 +28, 75) #2ndship 
        fill(185,0,255)
        ellipse(xCoord2, yCoord, 15, 40) 
        xCoord2 += xSpeed2 
        if xCoord2 + 28 >= 200 or xCoord2 -28 <= 120: 
            xSpeed2 = -xSpeed2  
    
    if LoLo.shotShip3 == False:
        fill(155)
        triangle(xCoord3 -28,yCoord+25, xCoord3, 20, xCoord3 +28, 75) #3rdship
        fill(185,0,255)
        ellipse(xCoord3, yCoord, 15, 40) 
        xCoord3 += xSpeed3 
        if xCoord3 +28 >= 280 or xCoord3 - 28 <= 210: 
            xSpeed3 = -xSpeed3 
    if LoLo.shotShip4 == False:
        fill(155)
        triangle(xCoord4 - 28, yCoord+25, xCoord4, 20,xCoord4 +28, 75) #4thship
        fill(185,0,255)
        ellipse(xCoord4, yCoord, 15, 40) 
        xCoord4 += xSpeed4 
        if xCoord4 +28 >= 380 or xCoord4 - 28 <= 300: 
            xSpeed4 = -xSpeed4
    if LoLo.shotShip5 == False:
        fill(155)
        triangle(xCoord5-28, yCoord2 + 30, xCoord5, 105, xCoord5+28, 165) #5thship
        fill(0, 185, 255)
        ellipse(xCoord5, yCoord2, 15, 40) 
        xCoord5 += xSpeed5 
        if xCoord5 +28 >= 156 or xCoord5 - 28 <= 60: 
            xSpeed5 = -xSpeed5 

    if LoLo.shotShip6 == False:
        fill(155)
        triangle(xCoord6 -28, yCoord2 +30, xCoord6, 105, xCoord6+28, 165) #6thship
        fill(0, 185, 255)
        ellipse(xCoord6, yCoord2, 15, 40) 
        xCoord6 += xSpeed6 
        if xCoord6 +28 >= 250 or xCoord6 <= 190: 
            xSpeed6 = -xSpeed6 
     
    if LoLo.shotShip7 == False:
        fill(155)
        triangle(xCoord7 - 28, yCoord2 + 30, xCoord7, 105, xCoord7 + 28, 165) #7thship
        fill(0, 185, 255)
        ellipse(xCoord7, yCoord2, 15, 40) 
        xCoord7 += xSpeed7 
        if xCoord7 +28 >= 320  or xCoord7 - 28 <= 280: 
            xSpeed7 = -xSpeed7 
    
    
    
   
