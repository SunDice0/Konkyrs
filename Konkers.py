from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout,QVBoxLayout, QLabel,QMessageBox,QRadioButton
def winner():
    window = QMessageBox()
    window.setText("Правильно! Ви виграли гіроскутер")
    window.exec()
def looser():
    window = QMessageBox()
    window.setText("Ні, в 2015 році. Ви виграли фірмовий плакат")
    window.exec()

app = QApplication([])
win = QWidget()
win.setWindowTitle("Конкурс від Crazy People")
win.resize(400,200)
win.move(100,100)
question =  QLabel("В якому році канал отримав 'золоту кнопку' від Youtube?")
btn_answer1 =  QRadioButton("2005")
btn_answer2 =  QRadioButton("2010")
btn_answer3 =  QRadioButton("2015")
btn_answer4 =  QRadioButton("2020")
line = QVBoxLayout()
line.addWidget(question,alignment = Qt.AlignCenter)
line1 = QHBoxLayout()
line1.addWidget(btn_answer1,alignment = Qt.AlignCenter)
line1.addWidget(btn_answer2,alignment = Qt.AlignCenter)
line2 =QHBoxLayout()
line2.addWidget(btn_answer3,alignment = Qt.AlignCenter)
line2.addWidget(btn_answer4,alignment = Qt.AlignCenter)

line.addLayout(line1)
line.addLayout(line2)
win.setLayout(line)

btn_answer3.clicked.connect(winner)
btn_answer1.clicked.connect(looser)
btn_answer2.clicked.connect(looser)
btn_answer4.clicked.connect(looser)

win.show()
app.exec()
