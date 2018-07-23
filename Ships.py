def visuals():
    #size(400,600)
    fill(30,90,100)
    rect(100,100,50,50)
    triangle(30,535,58,300,86,535)
    ellipse(56, 46, 55, 55)
    
def ships():
    background(0)
    #Player Ship
    noStroke()
    fill(255,0,0)
    rect(mouseX,500,35,35)
    fill(255)
    triangle(mouseX-3, 535, mouseX+17, 480, mouseX+38, 535)
    fill(50,120,255)
    ellipse(mouseX+17, 513, 13, 33)
    
    #Bad Guy Ships 
    fill(155)
    triangle(30, 75, 58, 20, 86, 75)
    fill(185,0,255)
    ellipse(58, 50, 15, 40)
