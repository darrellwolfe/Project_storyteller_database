import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle('Interactive Window')
label = QLabel('Hello, welcome to the popup!', parent=window)
label.move(50, 50)
window.resize(300, 200)
window.show()
app.exec_()
