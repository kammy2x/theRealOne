xSpeed = 2 
xSpeed2 = 2 
xSpeed3 = 2 
xSpeed4 = 2 
xCoord = 58 
yCoord = 50 
xCoord2 = 148 
xCoord3 = 238 
xCoord4 = 328

def themBoys(): 
    global xCoord, yCoord, xCoord2, xCoord3, xCoord4, xSpeed, xSpeed2, xSpeed3, xSpeed4  
    
    fill(155)
    triangle(xCoord -28,yCoord+25, xCoord, 20, xCoord +28, 75) #1stship
    fill(185,0,255) 
    ellipse(xCoord,yCoord,15,40) 
    xCoord += xSpeed 
    if xCoord +28 >= 120 or xCoord - 28<= 0: 
        xSpeed = -xSpeed
     
    fill(155)
    triangle(xCoord2 -28, yCoord+25, xCoord2, 20, xCoord2 +28, 75) #2ndship 
    fill(185,0,255)
    ellipse(xCoord2, yCoord, 15, 40) 
    xCoord2 += xSpeed2 
    if xCoord2 + 28 >= 210 or xCoord2 -28 <= 119: 
        xSpeed2 = -xSpeed2 
    
    
    fill(155)
    triangle(xCoord3 -28,yCoord+25, xCoord3, 20, xCoord3 +28, 75) #3rdship
    fill(185,0,255)
    ellipse(xCoord3, yCoord, 15, 40) 
    xCoord3 += xSpeed3 
    if xCoord3 +28 >= 300 or xCoord3 - 28 <= 209: 
        xSpeed3 = -xSpeed3
    
    fill(155)
    triangle(xCoord4 - 28, yCoord+25, xCoord4, 20,xCoord4 +28, 75) #4thship
    fill(185,0,255)
    ellipse(xCoord4, yCoord, 15, 40) 
    xCoord4 += xSpeed4 
    if xCoord4 +28 >= 400 or xCoord4 - 28 <= 299: 
        xSpeed4 = -xSpeed4
    
    fill(155)
    triangle(80, 165, 108, 105, 136, 165) #5thship
    fill(0, 185, 255)
    ellipse(108, 135, 15, 40)
    
    fill(155)
    triangle(170, 165, 198, 105, 226, 165) #6thship
    fill(0, 185, 255)
    ellipse(198, 135, 15, 40)
    
    fill(155)
    triangle(260, 165, 288, 105, 316, 165) #7thship
    fill(0, 185, 255)
    ellipse(288, 135, 15, 40)
    
    
   
