import pygame as pg
import configparser, json

# ----------- to do list -----------
# side panels (left and right) - done
# color scheme (dark and white) - done
# side panel left item categories - done
# side panel right item details button etc
# side panel expand button animation - done
# item cards - done
# main content - done
# main content item details button etc - done
# buttons
# add to cart - done
# remove from cart

# search bar
# search bar filter
# cart
# checkout
# settings
# scroll wheel
# about
# help



# receipts
# print receipt
# covnert to pdf
 # make own module {pussy.py} - module
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
pg.display.set_caption("7-Evelyn Beta 0.1")
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
    panels = (40, 40, 40)

#light mode
if theme == "light":
    background = (255, 255, 255)
    foreground = (200, 200, 200)
    highlight = (50, 50, 50)
    panels = (220, 220, 220)



# class lng to ng panels wag maguluhan
class side_panel:
    def __init__(self):
        # panels to
        self.left_panel = pg.Surface((100, height))
        self.left_panel.fill(panels)
        self.right_panel = pg.Surface((200, height))
        self.right_panel.fill(panels)
        self.expand_button = pg.Surface((100, height))
        self.expand_button.fill(highlight)
        self.trigger_expand = False
        self.animation_speed = 15
        self.animate_frame_left_panel = 0

        self.scroll_offset_y = 0

        #item cards

        self.animate_frame_item_category = 0

        self.item_card = pg.Surface((200, 250))
        self.item_card.fill(foreground)
        self.selected_category = None  # Add this line to store the selected category
        self.mouse_pressed = False  # Initialize mouse_pressed attribute

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
                self.left_panel.fill(panels)
                self.animate_frame_left_panel -= self.animation_speed

                if self.animate_frame_left_panel <= 0:
                    self.animate_frame_left_panel = 0

        if self.trigger_expand:
            self.left_panel = pg.Surface((self.animate_frame_left_panel + 100, height))
            self.left_panel.fill(panels)
            self.animate_frame_left_panel += self.animation_speed

            if self.animate_frame_left_panel >= 130:
                self.animate_frame_left_panel = 130


    def scroll_wheel(self, event):

        #""" Scroll wheel trigger offset soo plus minus yung offset sa Y value ng items """

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                print("Scrolled up")
                self.scroll_offset_y -= 50
            elif event.button == 5:  
                print("Scrolled down")
                self.scroll_offset_y += 50

        if self.scroll_offset_y >= 0:
            self.scroll_offset_y = 0


    def items(self, category=None):
        with open('data/item-data.json', 'r') as file:
            self.data_items = json.load(file)

        #font = pg.font.Font(None, 12)
        x_offset = 100
        y_offset = 100
        card_width = 200
        card_height = 250
        max_cards_per_row = 4
        card_spacing = 30

        items_to_display = self.data_items['items']
        if category:
            items_to_display = [item for item in items_to_display if item['category'] == category]

        for index, item in enumerate(items_to_display):
            if index % max_cards_per_row == 0 and index != 0:
                x_offset = 100
                y_offset += card_height + card_spacing

            item_card = pg.Surface((card_width, card_height))
            item_card.fill(foreground)
            window.blit(item_card, (x_offset + 50, y_offset + self.scroll_offset_y))

            # ================================ Item text/Image =====================================================
            # Load and display item image
            try:
                item_image = pg.image.load(item['image'])
                item_image = pg.transform.scale(item_image, (card_width - 20, card_height - 85))
                image_rect = item_image.get_rect(center=(x_offset + card_width // 2 + 50, y_offset + self.scroll_offset_y + 95))
                window.blit(item_image, image_rect)
            except FileNotFoundError:
                pass
                #print(f"Image file not found: {item['image']}")
            
            font = pg.font.Font(None, 23)
            text = font.render(item['name'], True, highlight)
            text_rect = text.get_rect(center=(x_offset + card_width // 2 + 50, y_offset + self.scroll_offset_y + 195))
            window.blit(text, text_rect)


            # ================================ "Add to Cart" button =====================================================
            add_to_cart_button = pg.Surface((card_width - 20, 30))
            add_to_cart_button.fill(highlight)
            button_rect = add_to_cart_button.get_rect(topleft=(x_offset + 60, y_offset + self.scroll_offset_y + card_height - 40))
            window.blit(add_to_cart_button, button_rect.topleft)

            font = pg.font.Font(None, 24)
            button_text = font.render("Add to Cart", True, background)
            window.blit(button_text, (button_rect.x + 45, button_rect.y + 7))

            if button_rect.collidepoint(pg.mouse.get_pos()):
                if pg.mouse.get_pressed()[0] and not self.mouse_pressed:
                    self.add_to_cart(item)
                    self.mouse_pressed = True
                elif not pg.mouse.get_pressed()[0]:
                    self.mouse_pressed = False

            x_offset += card_width + card_spacing

    def add_to_cart(self, item):
        try:
            with open('data/user_data.json', 'r') as file:
                cart_data = json.load(file)
        except FileNotFoundError:
            cart_data = []

        cart_data.append(item)

        with open('data/user_data.json', 'w') as file:
            json.dump(cart_data, file, indent=4)

    def left_pan_category(self):
        font = pg.font.Font(None, 32)
        y_offset = 20
        for item in self.data_items['categories']:
            self.item_category = pg.Surface((50, 50))
            self.item_category.fill(foreground)
            window.blit(self.item_category, (25 , y_offset))

            text = font.render(item['name'], True, highlight)
            text.set_alpha(self.animate_frame_left_panel)
            window.blit(text, (100, y_offset + 14))

            category_rect = self.item_category.get_rect(topleft=(25, y_offset))
            if category_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                self.selected_category = item['category']
                print(f"Category selected: {self.selected_category}")

            y_offset += 90

        self.animate_frame_item_category += self.animation_speed

        if self.trigger_expand:
            if self.animate_frame_item_category >= 255:
                self.animate_frame_item_category = 255


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
            with open('data/user_data.json', 'w') as file:
                json.dump([], file, indent=0)
                
            pg.quit()

        panel.scroll_wheel(event)

# main loop dito lahat ng functions na kailangan
while True:
    event_handler()
    panel.panels()
    panel.items(panel.selected_category)
    panel.draw()
    panel.left_pan_category()
    pg.display.update()
    pg.time.Clock().tick(60)