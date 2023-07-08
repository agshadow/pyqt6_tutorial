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
        # self.button.released.connect(self.the_button_was_released)
        self.button.pressed.connect(self.the_button_was_pressed)
        self.button.clicked.connect(self.the_button_was_released)
        # set the control widget of the Window.
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self, checked):
        print(checked)

    def the_button_was_released(self):
        self.button.setText("You already clicked me.")
        # self.button.setEnabled(False)
        self.setWindowTitle("My oneShot App")

    def the_button_was_pressed(self):
        self.button.setText("Press Me!")
        self.setWindowTitle("A new window title")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
