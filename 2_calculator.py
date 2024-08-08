from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit,QLabel,QPushButton, QMessageBox

# for actions on clicking button..........
def on_click():
    button=app.sender()
    element=button.text()
    try:
        if element=="=":
            # using in-built function "eval" to evaluate string and gives result into float value
            result.setText(result.text() + str(eval(equation.text())))
            equation.setText("")
        elif element=="a\u00B2":
            square=equation.text()[-1]
            equation.setText(equation.text()+f"*{square}")
            result.setText("Result:")
        else:
            equation.setText(equation.text() + element)
            result.setText("Result:")
    except:
        QMessageBox.information(main_window, "ERROR", "INVALID INPUT")

# main application........
app=QApplication([])

# main window.............
main_window=QMainWindow()
main_window.setWindowTitle("My Application")
main_window.setFixedSize(400,640)

# central widget...........
central_widget=QWidget()
# central_widget.setStyleSheet("background-color: black;")
main_window.setCentralWidget(central_widget)

#main layout................
main_lay=QVBoxLayout()
central_widget.setLayout(main_lay)


#for dividing sections (display and buttons)
display=QVBoxLayout()
buttons_box=QHBoxLayout()
main_lay.addLayout(display)
main_lay.addLayout(buttons_box)


# adding equation box and result box...........................
equation=QLineEdit()
display.addWidget(equation)
result=QLabel("Result:")
display.addWidget(result)

#for numbers box and operators box........................
numbers=QGridLayout()
buttons_box.addLayout(numbers)
operators=QGridLayout()
buttons_box.addLayout(operators)

# adding number buttons in numbers box....................
lis1=["7","8","9","4","5","6","1","2","3","0","00","."]
row1,col1=0,0
for i in lis1:
    btn=QPushButton(i)
    numbers.addWidget(btn,row1,col1,1,1)
    btn.clicked.connect(on_click)
    col1+=1
    if col1==3:
        col1=0
        row1+=1

# adding operators buttons in operators box....................
lis2=["*","-","/","+","=","a\u00B2"]
row2,col2=0,0
for i in lis2:
    btn=QPushButton(i)
    operators.addWidget(btn,row1,col1,1,1)
    btn.clicked.connect(on_click)
    col1+=1
    if col1==2:
        col1=0
        row1+=1

# showing window and looping
main_window.show()
app.exec_()
