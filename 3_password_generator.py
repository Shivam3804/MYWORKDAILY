from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QComboBox, QPushButton, QMessageBox
from PyQt5.QtGui import QIntValidator
import random
import string


def on_click():
    how_long=int(length.text())
    level=drop_down.currentText()
    if level=="Easy":
        # password with only letters
        lis=string.ascii_letters
        result="".join(random.sample(lis,how_long))
    elif level=="Medium":
        # password with letters and numbers
        lis=string.ascii_letters +string.digits
        result="".join(random.sample(lis,how_long))
    elif level=="Hard":
        # password with letters, numbers and symbols
        lis=string.ascii_letters + string.digits + string.punctuation
        result="".join(random.sample(lis,how_long))
    else:
        QMessageBox.information(window,"ERROR", "INVALID INPUT")     
    
    password.setText(result)

#main app
app=QApplication([])

#main window
window=QMainWindow()
window.setWindowTitle("PASSWORD GENERATOR")
window.setFixedSize(600,250)
app.setActiveWindow(window)

#central widget
central_widget=QWidget()
central_widget.setStyleSheet("background-color: burlywood;")
window.setCentralWidget(central_widget)

#main layout....
lay1=QVBoxLayout()
central_widget.setLayout(lay1)

#input for length of password
length=QLineEdit()
length.setStyleSheet("background-color: sienna; color:wheat; font-size:20px")
lay1.addWidget(length)
length.setPlaceholderText("Enter the length of password:")

#restrict character or large numbers as input
validator=QIntValidator(1,50)
length.setValidator(validator)

#drop-down for difficulty
drop_down=QComboBox()
drop_down.setStyleSheet("background-color: sienna; color:black; font-size:20px")
drop_down.addItems(["Easy","Medium","Hard"])
lay1.addWidget(drop_down)

#button for generating password
button=QPushButton("Generate")
button.setStyleSheet("background-color: sienna; color : black; font-size:20px")
lay1.addWidget(button)
button.clicked.connect(on_click)

#output to show resultant password
password=QLineEdit()
password.setStyleSheet("background-color: sienna; color:wheat; font-size:20px")
password.setPlaceholderText("Password")
password.setReadOnly(True)
lay1.addWidget(password)

# executing and looping the app
window.show()
app.exec_()



