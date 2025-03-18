import sys
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton
from PyQt5.QtGui import QIcon
import json

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Elevate beta 0.1")
window.resize(1280, 720)
window.show()


def setup_panels(window):
    
    main_layout = QHBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)

    expand_button = QPushButton("Expand")
    expand_button.setFixedWidth(100)
    main_layout.addWidget(expand_button)

    left_panel = QFrame()
    left_panel.setFrameShape(QFrame.StyledPanel)
    left_panel.setFixedWidth(100)
    main_layout.addWidget(left_panel)

    def panel_button():
        with open('data/item-data.json', 'r') as file:
            button_data = json.load(file)

        button_layout = QVBoxLayout()
        for item in button_data['items']:
            button = QPushButton(item['category'])
            if 'image' in item:
                button.setIcon(QIcon(item['image']))
                print("Image found")
            button_layout.addWidget(button)

        left_panel.setLayout(button_layout)

        content = QWidget()
        main_layout.addWidget(content)
    panel_button()

    right_panel = QFrame()
    right_panel.setFrameShape(QFrame.StyledPanel)
    right_panel.setFixedWidth(300)
    main_layout.addWidget(right_panel)


    def expand_left_panel():
        if left_panel.width() == 100:
            left_panel.setFixedWidth(300)
            for i in range(left_panel.layout().count()):
                button = left_panel.layout().itemAt(i).widget()
                button.setText(button.text() + " - Expanded")
        else:
            left_panel.setFixedWidth(100)
            for i in range(left_panel.layout().count()):
                button = left_panel.layout().itemAt(i).widget()
                button.setText(button.text().replace(" - Expanded", ""))

    expand_button.clicked.connect(expand_left_panel)

    window.setLayout(main_layout)

setup_panels(window)

sys.exit(app.exec_())