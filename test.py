import sys
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton
import json


with open('data/item-data.json', 'r') as file:
    button_data = json.load(file)


for item in button_data['items']:
    print(item['category'])
