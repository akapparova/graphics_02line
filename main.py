from display import *
from draw import *

screen = new_screen()



//NEED TO MAKE AN ACTUAL IMAGE WITH THIS!!!!!!




color = [ 100, 100, 100 ]
draw_line (100,400,230, 300, screen, color)
draw_line (270,300,400, 400, screen, color)

color = [ 80, 80, 80 ]
draw_line (150,270,200, 270, screen, color) #SLOPE 0

color = [ 70, 70, 70]
draw_line (250,200,250, 250, screen, color) #SLOPE UNDEFINED

color = [ 60, 60, 60 ]
draw_line (150,120, 380, 120, screen, color)
draw_line (120,90, 150, 120, screen, color) #SLOPE 1
draw_line (380,120, 410, 90, screen, color) #SLOPE -1






save_extension(screen, 'img.png')