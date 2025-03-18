import pygame as pg
import configparser, json

# ----------- to do list -----------
# side panels (left and right) - done
# color scheme (dark and white) - done
# side panel left item categories 
# side panel right item details button etc
# side panel expand button animation - done
# item cards - done
# main content
# main content item details button etc
# search bar
# search bar filter
# cart
# checkout
# settings
# scroll wheel
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
        self.expand_button = pg.Surface((100, height))
        self.expand_button.fill(highlight)
        self.trigger_expand = False
        self.animation_speed = 15
        self.animate_frame_left_panel = 0


        #item cards
        self.item_card = pg.Surface((200, 250))
        self.item_card.fill(foreground)

    def panels(self):
        # trigger ng animation
        left_panel_rect = self.left_panel.get_rect(topleft=(0, 0))
        if left_panel_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            if not self.trigger_expand:
                self.trigger_expand = True
                print("Panel exp")
            

        elif not left_panel_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            if self.trigger_expand:
                self.trigger_expand = False
                print("Panel col")

        if self.trigger_expand == False:
                self.left_panel = pg.Surface((self.animate_frame_left_panel + 100, height))
                self.left_panel.fill(foreground)
                self.animate_frame_left_panel -= self.animation_speed

                if self.animate_frame_left_panel <= 0:
                    self.animate_frame_left_panel = 0

        if self.trigger_expand:
            self.left_panel = pg.Surface((self.animate_frame_left_panel + 100, height))
            self.left_panel.fill(foreground)
            self.animate_frame_left_panel += self.animation_speed

            if self.animate_frame_left_panel >= 200:
                self.animate_frame_left_panel = 200


    def items(self):
        with open('data/item-data.json', 'r') as file:
            data_items = json.load(file)

        x_offset = 100
        y_offset = 100
        card_width = 200
        card_height = 250
        max_cards_per_row = 4
        card_spacing = 30

        for index, item in enumerate(data_items['items']):
            if index % max_cards_per_row == 0 and index != 0:
                x_offset = 100
                y_offset += card_height + card_spacing

            item_card = pg.Surface((card_width, card_height))
            item_card.fill(foreground)
            window.blit(item_card, (x_offset + 50, y_offset))
            x_offset += card_width + card_spacing


    def draw(self):
        # lahat ng elems dto ddraw
        #window.blit(self.expand_button, (0, 0))

        window.blit(self.left_panel, (0, 0))
        window.blit(self.right_panel, (width - 200, 0))
        #window.blit(self.item_card, (150, height - height + 100))

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
    panel.panels()
    panel.items()
    pg.display.update()
    pg.time.Clock().tick(60)