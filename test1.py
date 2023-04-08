from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def test():
    print("salaaaaaaam")



my_app = QApplication([])

loader = QUiLoader()
window = loader.load("episode17/untitled.ui")
window.show()

window.pushButton.clicked.connect(test)


my_app.exec()