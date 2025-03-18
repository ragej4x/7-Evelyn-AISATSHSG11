import pygame as pg
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
width = int(config['Window']['width'])
height = int(config['Window']['height'])

window = pg.display.set_mode((width, height))
pg.display.set_caption("Elevate Beta 0.1")
pg.display.set_icon(pg.image.load("data/icon.png"))
pg.init()

def event_handler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

while True:
    event_handler()
    pg.display.update()