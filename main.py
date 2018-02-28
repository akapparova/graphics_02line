from display import *
import random
from draw import *

screen = new_screen()

def rand():
	return random.randint(0,XRES)

for each in range(YRES):
	draw_line(0, 0, rand(), rand(), screen, [rand(), rand(), rand()])



save_extension(screen, 'img.png')