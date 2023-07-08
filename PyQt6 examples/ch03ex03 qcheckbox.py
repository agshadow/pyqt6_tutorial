import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    QListWidget,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Unchecked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == 2, s)
        print(1 == Qt.CheckState.Checked, s)
        print(Qt.CheckState.Checked)
        print(f"{s=}")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
