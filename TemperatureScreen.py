import pygame
import time
import random
# Import the ADS1x15 module.
import Adafruit_ADS1x15

pygame.init()


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
GAIN = 1

# Start continuous ADC conversions on channel 0 using the previously set gain value.
adc.start_adc(1 , gain=GAIN)

display_width = 800
display_height =450 

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tempoify')

##icon = pygame.image.load("bookshelves.gif")
##pygame.display.set_icon(icon)

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)


##img = pygame.image.load('bookshelves.gif')
# appleimg = pygame.image.load('apple.png')

##def score(score):
##
##    text = smallfont.render("Score: "+str(score), True, black)
##    gameDisplay.blit(text, [0,0])


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = round(buttonx + (buttonwidth / 2)), round(buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    x = int(round((display_width / 2)))
    y = int(round((display_height / 2) + y_displace))

    textRect.center = x, y
    gameDisplay.blit(textSurf, textRect)


def pause():

    paused = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        

        clock.tick(5)
        
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "next":
                import Main_Game

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

        text_to_button(text, black, x, y, width, height)


def getValues():
    # Read channel 0 for 5 seconds and print out its values.
    start = time.time()
    while (time.time() - start) <= 1.0:
        # Read the last ADC conversion value and print it out.
        value = adc.get_last_result()
    if value <= 19999:
        # this will return the slow song
        return 20
    elif value >= 21999:
        # fast song
        return 46
    else:
        # medium
        return 30
        

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Let's start. First, touch the temperature sensor :)", black, 10)
        message_to_screen("Don't be afraid, it won't kill you... yet *smile*", black, 50)

       # button("Play", 150, 375, 100, 50, green, light_green, action="play")

        button("Next", 150, 300, 100, 50, green, light_green, action="next")
        pygame.display.update()
        clock.tick(15)

game_intro()
adc.stop_adc()
