import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True

        self.setWindowTitle("My App")
        self.setMinimumSize(QSize(500, 500))

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.setFixedSize(QSize(100, 100))
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        # set the control widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
