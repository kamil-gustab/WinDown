# import os
# from time import sleep
#
#
# def shutdown(time=60, force='', reHour_operation=''):
#     """Shutting down computer after time (seconds) provided as argument"""
#
#     formatted_time = f'{time} sec' if time < 60 else f'{int(time/60)} min'
#     comment = f'Computer will be turned off in {formatted_time}. Usage of WinDown app.'
#     command = f'shutdown {force} {reHour_operation} /c "{comment}" /t {time} /s'
#     print(f'\n{command}\n')
#
#     os.system(command)
#
#     sleep(5)
#     os.system('shutdown -a')
#
#
# if __name__ == '__main__':
#
#     # shutdown(time=40, force='/f', reHour_operation='/r')
#     shutdown(time=40, force='/f')

from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("WinDown")

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        self.hour = int(datetime.now().strftime("%H"))-3
        self.minute = int(datetime.now().strftime("%M"))

        # creating a label to show the time
        self.label = QLabel(self)

        # setting geometry of label
        self.label.setGeometry(125, 100, 150, 70)

        # adding border to the label
        self.label.setStyleSheet("border : 4px solid black;")

        # setting text to the label
        time_now = f'{(self.hour):02d}:{(self.minute):02d}'
        self.label.setText(time_now)

        # setting font to the label
        self.label.setFont(QFont('Arial', 25))

        # setting alignment to the text of label
        self.label.setAlignment(Qt.AlignCenter)

        # managing hours
        hour_plus = QPushButton("+", self)
        hour_plus.setGeometry(160, 60, 30, 30)
        hour_plus.pressed.connect(self.Hour_plus)

        hour_minus = QPushButton("-", self)
        hour_minus.setGeometry(160, 180, 30, 30)
        hour_minus.pressed.connect(self.Hour_minus)

        # managing minutes
        min_plus = QPushButton("+", self)
        min_plus.setGeometry(210, 60, 30, 30)
        min_plus.pressed.connect(self.Min_plus)

        min_minus = QPushButton("-", self)
        min_minus.setGeometry(210, 180, 30, 30)
        min_minus.pressed.connect(self.Min_minus)

        # creating reset button
        re_set = QPushButton("Re-set", self)

        # setting geometry to the button
        re_set.setGeometry(125, 420, 150, 40)

        # add action to the method
        re_set.pressed.connect(self.Re_set)


    def showTime(self):
        time_now = f'{(self.hour):02d}:{(self.minute):02d}'
        self.label.setText(time_now)

    # Hour operations
    def Hour_plus(self):
        if self.hour != 23:
            self.hour += 1
            time_now = f'{(self.hour):02d}:{(self.minute):02d}'
            self.label.setText(time_now)

    def Hour_minus(self):
        if self.hour != 0:
            self.hour -= 1
            time_now = f'{(self.hour):02d}:{(self.minute):02d}'
            self.label.setText(time_now)

    # Minutes operations
    def Min_plus(self):
        if self.minute != 59:
            self.minute += 1
            time_now = f'{(self.hour):02d}:{(self.minute):02d}'
            self.label.setText(time_now)

    def Min_minus(self):
        if self.minute != 0:
            self.minute -= 1
            time_now = f'{(self.hour):02d}:{(self.minute):02d}'
            self.label.setText(time_now)

    def Re_set(self):
        # making flag to false
        self.flag = False

        # reseeting the hour
        self.hour = 0
        self.minute = 0

        # setting text to label
        # self.label.setText(str(self.hour))
        time_now = f'{(self.hour):02d}:{(self.minute):02d}'
        self.label.setText(time_now)

if __name__ == '__main__':

    # print("Current Time =", datetime.now().strftime("%H:%M"))

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
