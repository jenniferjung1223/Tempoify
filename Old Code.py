#################################################################
AUTHOR = JENNIFER JUNG, COLBY BOYD, ALAYNA JUNEAU
###################################################################

# values that needs to be imported 
from pygame import * # do we need the star? must check
pygame.init()
from Tkinter import *
from time import sleep
import RPi.GPIO as GPIO

######################

#Variables for program
WIDTH = 800
HEIGHT = 800

######################

# set to True to enable debugging
DEBUG = False

######################

class TitleScreen(object):
	def __init__(self):
    pass

class 
    
    


######################

class Main(Canvas):

	def __init__(self, master):
		Canvas.__init__(self, master)
  	self.config(bg = "white")
  	self.pack(fill = BOTH, expand = 1)
    
#######################

#create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Tempoify! :D")
s = Main(window)
# ait for the window to close
window.mainloop()
