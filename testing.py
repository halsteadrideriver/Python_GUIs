import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Press Event Example")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Click in this window", self)
        self.label.setGeometry(10, 10, 380, 180)
        self.label.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        """Overrides the default mousePressEvent handler."""
        if event.button() == Qt.LeftButton:
            self.label.setText("Left button pressed at ({}, {})".format(event.x(), event.y()))
        elif event.button() == Qt.RightButton:
            self.label.setText("Right button pressed at ({}, {})".format(event.x(), event.y()))
        else:
            self.label.setText("Other button pressed")
        # Optional: call the base class implementation
        super().mousePressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomWindow()
    ex.show()
    sys.exit(app.exec_())
