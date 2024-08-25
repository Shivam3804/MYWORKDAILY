from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QMessageBox
import random

num=0 # will represent the row of questions list
flag=0 # will check for right or wrong answer
index=0 # to check the number of questions are asked, so no question repeats
question_number=[0,1,2,3,4,5,6,7,8,9] # will be used so that no question is asked again

# list of questions, options and answers......
lis=[
      ["What is the capital of France?",["Berlin","Madrid","Paris", "Rome"], "Paris"],
      ["Which planet is known as the Red Planet?",["Earth","Mars","Jupiter", "Venus"], "Mars"],
      ["Who wrote the play \"Romeo and Juliet\"?",["Charles Dickens","William Shakespeare","Mark Twain", "Jane Austen"], "William Shakespeare"],
      ["Which element has the chemical symbol \'O\'?",["Oxygen","Silver","Osmium", "Mercury"], "Oxygen"],
      ["What is the largest mammal in the world?",["Elephant","Blue Whale","Giraffe", "Great White Shark"], "Blue Whale"],
      ["What is the largest organ in the human body?",["Heart","Liver","Skin", "Brain"], "Skin"],
      ["Who developed the theory of general relativity?",["Issac Newton","Albert Einstein","Nikola Tesla", "Galileo Galilei"], "Albert Einstein"],
      ["What is the positive square root of 64?",["9","8","1", "5"], "8"],
      ["Which programming language is primarily used for statistical computing and graphics?",["Python","Java","R", "C++"], "R"],
      ["What is the name of the first artificial Earth satellite launched by the Soviet Union in 1957?",["Voyager 1","Sputnik 1","Apollo 11", "Hubble Space Telescope"], "Sputnik 1"]
   ]

# when option is chosen............
def on_option():
   verify.setText("Is it your final answer?")
   btn.show()

# when final button is pressed..........
def on_click():

   if option_a.isChecked():
      answer=option_a.text()
   elif option_b.isChecked():
      answer=option_b.text()
   elif option_c.isChecked():
      answer=option_c.text()
   elif option_d.isChecked():
      answer=option_d.text()
   else:
      QMessageBox.information(main_window,"ERROR", "Please choose an option")
      return
   print(answer)

   global num, flag, index, lis

   if answer==lis[num][2] and index<=10:
      QMessageBox.information(main_window,"WIN!!!", "CORRECT ANSWER")
      btn.hide()
      verify.setText("Are You Reaady?\nSelect the Correct Option")
      shows[index].setStyleSheet("background-color: green")
      index+=1
      ask()
   elif answer!=lis[num][2]:
      shows[index].setStyleSheet("background-color: red")
      QMessageBox.information(main_window,"LOSE", f"INCORRECT ANSWER\n{9-i} correct answers")
      main_window.close()

   return


def ask():
   global num, question_number, lis

   if len(question_number)==0:
      QMessageBox.information(main_window,"DONE", "You answered all questions correctly")
      main_window.close()
      return

   
   shows[index].setStyleSheet("background-color: yellow")
   num=random.choice(question_number)
   question_number.remove(num)


   question.setText(lis[num][0])
   option_a.setText(lis[num][1][0])
   option_b.setText(lis[num][1][1])
   option_c.setText(lis[num][1][2])
   option_d.setText(lis[num][1][3])
   # to reset options
   option_a.setChecked(False)
   option_b.setChecked(False)
   option_c.setChecked(False)
   option_d.setChecked(False)

   return None



# app creation.........
app=QApplication([])

# setting a window............
main_window=QMainWindow()
main_window.setWindowTitle("Quiz App")
main_window.setFixedSize(650,400)
app.setActiveWindow(main_window)

# central widget.............
central_widget=QWidget()
main_window.setCentralWidget(central_widget)

# main layout...............
main_layout=QHBoxLayout()
central_widget.setLayout(main_layout)

# question and option section....................................................................................................
que_opt_widget=QWidget()    # to be able to set height and width
que_opt_widget.setFixedSize(487,400)
que_opt_layout=QVBoxLayout()
main_layout.addWidget(que_opt_widget)
que_opt_widget.setLayout(que_opt_layout)

# question display area........................
question=QLabel("")
question.setWordWrap(True)
que_opt_layout.addWidget(question)

# options display area.........................
option_lay=QGridLayout()
que_opt_layout.addLayout(option_lay)

# options.......................................
option_a=QRadioButton("")
option_lay.addWidget(option_a,0,0,1,1)
option_a.clicked.connect(on_option)

option_b=QRadioButton("")
option_lay.addWidget(option_b,0,1,1,1)
option_b.clicked.connect(on_option)

option_c=QRadioButton("")
option_lay.addWidget(option_c,1,0,1,1)
option_c.clicked.connect(on_option)

option_d=QRadioButton("")
option_lay.addWidget(option_d,1,1,1,1)
option_d.clicked.connect(on_option)

# answers section..................................................................................................................
answer_widget=QWidget()   # to be able to set height and width
answer_widget.setFixedSize(163,400)
answer_layout=QVBoxLayout()
main_layout.addWidget(answer_widget)
answer_widget.setLayout(answer_layout)

# to show total questions to answer..........
to_show=QVBoxLayout()
answer_layout.addLayout(to_show)

shows=[]
for i in range(10):
   show=QLineEdit()
   show.setReadOnly(True)
   show.setText(f"Question {i+1}")
   to_show.addWidget(show)
   shows.append(show)

# to verify for answer...........
verify=QLabel("Are You Reaady?\nSelect the Correct Option")
verify.setWordWrap(True)
answer_layout.addWidget(verify)

btn=QPushButton("Yes")
answer_layout.addWidget(btn)
btn.hide()
btn.clicked.connect(on_click)

#for asking questions
ask()


# for window running in loops........................................................................................................
main_window.show()
app.exec_()