import sys
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton
import json
import pygame


with open('data/item-data.json', 'r') as file:
    button_data = json.load(file)


for item in button_data['items']:
    print(item['category'])



    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Scroll Wheel Example")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    print("Mouse wheel scrolled up")
                elif event.button == 5:
                    print("Mouse wheel scrolled down")

        screen.fill((255, 255, 255))
        pygame.display.flip()

    pygame.quit()