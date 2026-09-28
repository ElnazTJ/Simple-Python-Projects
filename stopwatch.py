import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QIcon , QPixmap


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0, 0, 0 ,0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)  

        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        icon_path = os.path.join(os.path.dirname(__file__), "stopwatch_icon.png")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print("Icon not found:", icon_path)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
        QLabel , QPushButton{
            padding:20 px;
            font-weight: bold;
            font-family: calibri;

        }

        QLabel {
            font-size: 100px;
            background-color: hsl(198, 100%, 91%)
            }

        QPushButton {
            font-size: 50px;
            background-color: hsl(183, 66%, 97%);
        }

        QPushButton:hover {
        background-color: hsl(198, 100%, 91%);
        }
        
        QLabel {
            font-size: 150px;}
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)  # Update every 10 milliseconds

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00:00")    

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())