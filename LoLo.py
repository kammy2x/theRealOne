laserY = 75 
shotShip1 = False 
shotShip2 = False 
shotShip3 = False 
shotShip4 = False 
shotShip5 = False 
shotShip6 = False 
shotShip7 = False
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
   # ship1 = triangle(30, 75, 58, 20, 86, 75) 
    if mouseX > 400:
         line(pmouseX,pmouseY,mouseX,mouseY)
    if mouseY > 200:
         stroke(255,0,0)
         line(mouseX,mouseY,mouseX,laserY)
         
def shotShips():
    global laserY, shotShip1, shotShip2, shotShip3, shotShip4, shotShip5, shotShip6, shotShip7 
    
    if mousePressed and mouseX >=30 and mouseX <=86 and laserY<=75: #Conditional to make the first ship disappear
        shotShip1 = True  
  
    if mousePressed and mouseX >= 120 and mouseX <= 176 and laserY<=75: #Conditional to make the second ship disappear
        shotShip2 = True 

    if mousePressed and mouseX >= 210 and mouseX <= 266 and laserY<=75: 
        shotShip3= True
 
    if mousePressed and mouseX >=300 and mouseX<=356 and laserY<=75: 
        shotShip4 = True 
        
    if mousePressed and mouseX >=80 and mouseX <=136 and laserY<=165: 
        shotShip5 = True       

    if mousePressed and mouseX >=170 and mouseX <=226 and laserY<=165: 
        shotShip6 = True 
  
    if mousePressed and mouseX >=260 and mouseX<=316 and laserY<=165: 
        shotShip7 = True

    if shotShip1 == True and shotShip2 == True  and shotShip3 == True and shotShip4 == True and shotShip5 == True  and shotShip6 == True  and shotShip7 == True :
        fill(255,0,0)
        textSize(20)
        text("Level 1 Cleared", 135,300)
    if shotShip1 == False:
        textSize(20)
        text("CLICK TO START", 115,300)
    
                
