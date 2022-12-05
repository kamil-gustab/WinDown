import operations
import sys
from datetime import datetime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import \
    QApplication, QInputDialog, QLineEdit,\
    QMainWindow, QMessageBox, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinDown")
        self.setGeometry(100, 100, 400, 500)
        self.uicomponents()
        self.show()
        self.hour = int(datetime.now().strftime("%H"))

    # method for widgets
    def uicomponents(self):
        self.hour = int(datetime.now().strftime("%H"))
        self.minute = int(datetime.now().strftime("%M"))
        self.time_box = QPushButton(self)
        self.time_box.setGeometry(125, 120, 150, 70)
        self.time_box.setStyleSheet("border : 4px solid black;")
        shown_time = f'{self.hour:02d}:{self.minute:02d}'
        self.time_box.setText(shown_time)
        self.time_box.setFont(QFont('Arial', 25))

        # managing hours
        hour_plus = QPushButton("+", self)
        hour_plus.setGeometry(160, 80, 30, 30)
        hour_plus.pressed.connect(self.hour_plus)

        hour_minus = QPushButton("-", self)
        hour_minus.setGeometry(160, 200, 30, 30)
        hour_minus.pressed.connect(self.hour_minus)

        # managing minutes
        min_plus = QPushButton("+", self)
        min_plus.setGeometry(210, 80, 30, 30)
        min_plus.pressed.connect(self.min_plus)

        min_minus = QPushButton("-", self)
        min_minus.setGeometry(210, 200, 30, 30)
        min_minus.pressed.connect(self.min_minus)

        go_button = QPushButton("Request Shutdown", self)
        cancel_button = QPushButton("Cancel Shutdown", self)
        reset_button = QPushButton("Reset clock", self)

        go_button.setGeometry(125, 320, 150, 40)
        cancel_button.setGeometry(125, 370, 150, 40)
        reset_button.setGeometry(125, 420, 150, 40)

        go_button.pressed.connect(self.request_shutdown)
        cancel_button.pressed.connect(self.cancel_shutdown)
        reset_button.pressed.connect(self.reset_time)
        self.time_box.clicked.connect(lambda: self.show_input())

    # Hours operations
    def hour_plus(self):
        if self.hour < 23:
            self.hour += 1
            shown_time = f'{self.hour:02d}:{self.minute:02d}'
            self.time_box.setText(shown_time)

    def hour_minus(self):
        if self.hour > 0:
            self.hour -= 1
            shown_time = f'{self.hour:02d}:{self.minute:02d}'
            self.time_box.setText(shown_time)

    # Minutes operations
    def min_plus(self):
        if self.minute < 59:
            self.minute += 1
            shown_time = f'{self.hour:02d}:{self.minute:02d}'
            self.time_box.setText(shown_time)

    def min_minus(self):
        if self.minute > 0:
            self.minute -= 1
            shown_time = f'{self.hour:02d}:{self.minute:02d}'
            self.time_box.setText(shown_time)

    def reset_time(self):
        self.hour = int(datetime.now().strftime("%H"))
        self.minute = int(datetime.now().strftime("%M"))

        shown_time = f'{self.hour:02d}:{self.minute:02d}'
        self.time_box.setText(shown_time)

    def show_input(self):
        text, pressed = QInputDialog.getText(
            self, 'Time', 'Use "HH:MM" format.', QLineEdit.Normal, '')

        try:
            if pressed:
                if text[2] == ':' and len(text) == 5:
                    hour_ = int(text[:2])
                    if 0 <= hour_ <= 23:
                        self.hour = hour_
                    min_ = int(text[3:5])
                    if 0 <= min_ <= 59:
                        self.minute = min_
                    shown_time = f'{self.hour:02d}:{self.minute:02d}'
                    self.time_box.setText(shown_time)
        except ValueError:
            QMessageBox.about(self, 'Error',
                              'Wrong time format.\n'
                              'Use format: "HH:MM"\neg. 21:37')

    def request_shutdown(self):
        # translating string to datetime object
        time_now = datetime.now()
        shown_time = f'{str(time_now)[:11]}{self.hour:02d}:{self.minute:02d}'
        shown_time_obj = datetime.strptime(shown_time, '%Y-%m-%d %H:%M')

        # checking if requested shutdown isn't before actual time
        if shown_time_obj < datetime.now():
            return
        diff_in_sec = (shown_time_obj - time_now).seconds

        operations.shutdown(time=diff_in_sec)

    @staticmethod
    def cancel_shutdown():
        operations.cancel_shutdown()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
