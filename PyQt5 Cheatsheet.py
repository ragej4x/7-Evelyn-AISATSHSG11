# PyQt5 Cheatsheet

## Installation
```bash
pip install PyQt5
```

---
## Basic PyQt5 Window
```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5 Window")
window.resize(400, 300)
window.show()
sys.exit(app.exec_())
```

---
## Main Window with QPushButton
```python
from PyQt5.QtWidgets import QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)
        
        btn = QPushButton("Click Me", self)
        btn.setGeometry(200, 150, 200, 50)
        btn.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        print("Button Clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
```

---
## Widgets
### QLabel (Text Display)
```python
from PyQt5.QtWidgets import QLabel
label = QLabel("Hello, PyQt5!", window)
label.move(100, 50)
```

### QLineEdit (Input Field)
```python
from PyQt5.QtWidgets import QLineEdit
text_input = QLineEdit(window)
text_input.move(100, 80)
```

### QTextEdit (Multi-line Text Field)
```python
from PyQt5.QtWidgets import QTextEdit
text_area = QTextEdit(window)
text_area.setGeometry(100, 120, 200, 100)
```

### QCheckBox (Checkbox)
```python
from PyQt5.QtWidgets import QCheckBox
checkbox = QCheckBox("Accept Terms", window)
checkbox.move(100, 250)
```

### QRadioButton (Radio Button)
```python
from PyQt5.QtWidgets import QRadioButton
radio_button = QRadioButton("Option 1", window)
radio_button.move(100, 280)
```

### QComboBox (Dropdown)
```python
from PyQt5.QtWidgets import QComboBox
combo_box = QComboBox(window)
combo_box.addItems(["Option 1", "Option 2", "Option 3"])
combo_box.move(100, 310)
```

### QListWidget (List Box)
```python
from PyQt5.QtWidgets import QListWidget
list_widget = QListWidget(window)
list_widget.addItems(["Item 1", "Item 2", "Item 3"])
list_widget.setGeometry(100, 340, 200, 100)
```

### QLabel with Image (Displaying an Image)
```python
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

image_label = QLabel(window)
image_label.setPixmap(QPixmap("path/to/image.png"))
image_label.setGeometry(100, 450, 200, 150)
```

---
## Adding a Side Panel (QDockWidget)
```python
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window with Side Panel")
        self.setGeometry(100, 100, 600, 400)
        
        dock = QDockWidget("Side Panel", self)
        dock.setWidget(QTextEdit("This is a side panel."))
        self.addDockWidget(3, dock)  # 3 corresponds to Qt.RightDockWidgetArea

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
```

---
## Layouts
### QVBoxLayout (Vertical Layout)
```python
from PyQt5.QtWidgets import QVBoxLayout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(text_input)
window.setLayout(layout)
```

### QHBoxLayout (Horizontal Layout)
```python
from PyQt5.QtWidgets import QHBoxLayout
layout = QHBoxLayout()
layout.addWidget(label)
layout.addWidget(text_input)
window.setLayout(layout)
```

### QGridLayout (Grid Layout)
```python
from PyQt5.QtWidgets import QGridLayout
layout = QGridLayout()
layout.addWidget(label, 0, 0)
layout.addWidget(text_input, 0, 1)
window.setLayout(layout)
```

---
## Signals & Slots
```python
button.clicked.connect(lambda: print("Button Clicked"))
checkbox.stateChanged.connect(lambda: print("Checkbox Changed"))
text_input.textChanged.connect(lambda text: print(f"Input: {text}"))
```

---
## Dialogs
### Message Box
```python
from PyQt5.QtWidgets import QMessageBox
msg = QMessageBox()
msg.setText("This is a message box")
msg.exec_()
```

### File Dialog
```python
from PyQt5.QtWidgets import QFileDialog
filename, _ = QFileDialog.getOpenFileName()
```

---
## Menus & Toolbars
```python
menu_bar = window.menuBar()
file_menu = menu_bar.addMenu("File")
```

---
## Running the Application
```python
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
```

