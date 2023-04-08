from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def sub():
    global a
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def result():
    b = int(main_window.txt_box.text())
    c = a - b
    main_window.txt_box.setText(str(c))


app = QApplication([])

loader = QUiLoader()
main_window = loader.load("episode17\calculator_ui.ui")
main_window.show()

main_window.btn_sub.clicked.connect(sub)
main_window.btn_result.clicked.connect(result)


app.exec()
