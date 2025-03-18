import pygame as pg
import configparser

# ----------- to do list -----------
# side panels (left and right)
# color scheme (dark and white)
# side panel left item categories
# side panel right item details button etc
# main content
# main content item details button etc
# cart
# checkout
# search
# settings
# about
# help
#----------------------------------








# ---- config ----
# dito nyo ilalagay yung mga settings nyo sa window
config = configparser.ConfigParser()
config.read('config.ini')
width = int(config['Window']['width'])
height = int(config['Window']['height'])
theme = config['Window']['theme']

# ---- window settings ----

window = pg.display.set_mode((width, height))
pg.display.set_caption("Elevate Beta 0.1")
pg.display.set_icon(pg.image.load("data/icon.png"))
pg.init()


# ---- color scheme to for dark mode----
# mag lagay lng kayo kung anong gusto nyong color scheme themes
# dito kayo mag base https://colorhunt.co/

#dark mode
if theme == "dark":
    background = (30, 30, 30)
    foreground = (50, 50, 50)
    highlight = (200, 200, 200)


#white mode
if theme == "white":
    background = (255, 255, 255)
    foreground = (200, 200, 200)
    highlight = (50, 50, 50)



# class lng to ng panels wag maguluhan
class side_panel:
    def __init__(self):
        # panels to
        self.left_panel = pg.Surface((100, height))
        self.left_panel.fill(foreground)
        self.right_panel = pg.Surface((200, height))
        self.right_panel.fill(foreground)
    
    def animate(self):
        pass

    def draw(self):
        # lahat ng elems dto ddraw
        window.blit(self.left_panel, (0, 0))
        window.blit(self.right_panel, (width - 200, 0))

panel = side_panel()

# event handler dito lahat ng events
def event_handler():
    window.fill(background)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()


# main loop dito lahat ng functions na kailangan
while True:
    event_handler()
    panel.draw()
    pg.display.update()