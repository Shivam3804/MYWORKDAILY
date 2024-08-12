from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QMessageBox
import requests
import time
import json

# finding results
def on_click():
    try:
        # date and location for query
        date=time.strftime("%Y-%m-%d")
        loca=city.text()
        # API request
        url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{loca}/{date}?"
        key="2NNHMWSURZ95ACPMSLQNPJNF2"
        var=requests.get(url, params={'key':key})
        # response
        results=var.json()
        print(results)
        # farenheit to celcius
        C=(results['currentConditions']['temp']-32)*5/9
        temp.setText(f"{round(C,2)}")
        H=results['currentConditions']['humidity']
        humid.setText(f"{round(H,2)}")
        desc=results['description']
        description.setText(f"{city.text()}\n{desc}")
        city.setText("")
    except:
        QMessageBox.information(window,"ERROR", "Location Not Found\nEnter The Correct Location")

# main application
app=QApplication([])

# main window
window=QMainWindow()
window.setWindowTitle("Weather Forecast")
window.setStyleSheet("font-size:20px")
window.setFixedSize(500,300)
app.setActiveWindow(window)

# main widget
central_widget=QWidget()
window.setCentralWidget(central_widget)

# main layout
main_layout=QVBoxLayout()
central_widget.setLayout(main_layout)

# inputs for city
city=QLineEdit()
city.setPlaceholderText("Enter the city:")
city.setStyleSheet("margin: 10px 0px")
main_layout.addWidget(city)

# button to generate the output
buttton=QPushButton("Search")
buttton.setStyleSheet("margin: 10px 0px")
main_layout.addWidget(buttton)
buttton.clicked.connect(on_click)

# for showing output
final_output=QVBoxLayout()
main_layout.addLayout(final_output)

# for numerical results
num_output=QHBoxLayout()
final_output.addLayout(num_output)

# for tempreture
label_t=QLabel("Tempreture(C)")
temp=QLineEdit()
temp.setReadOnly(True)
num_output.addWidget(label_t)
num_output.addWidget(temp)

# for humidity
label_h=QLabel("Humidity(%)")
humid=QLineEdit()
humid.setReadOnly(True)
num_output.addWidget(label_h)
num_output.addWidget(humid)

# for description of conditions
description=QLabel("")
description.setStyleSheet("margin: 10px 0px")
description.setWordWrap(True)
final_output.addWidget(description)


# for running window in loops
window.show()
app.exec_()
