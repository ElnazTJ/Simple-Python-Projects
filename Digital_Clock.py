import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 400, 100)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("Font-size: 150px; color:hsl(111, 100%, 50%); background-color: black;")

        Font_id=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        Font_family=QFontDatabase.applicationFontFamilies(Font_id)[0]
        my_font=QFont(Font_family, 100)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())