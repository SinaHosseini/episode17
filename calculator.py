import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def number():
    ...


def sub():
    global a, operator
    operator = "sub"
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def sum():
    global a, operator
    operator = "sum"
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def div():
    global a, operator
    operator = "div"
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def mul():
    global a, operator
    operator = "mul"
    a = int(main_window.txt_box.text())
    main_window.txt_box.setText("")


def perc():
    global percent
    percent = True


def sqrt():
    a = int(main_window.txt_box.text())
    b = math.sqrt(a)
    main_window.txt_box.setText(str(b))


def sin():
    a = int(main_window.txt_box.text())
    a = a / 180 * math.pi
    b = math.sin(a)
    main_window.txt_box.setText(str(b))


def cos():
    a = int(main_window.txt_box.text())
    a = a / 180 * math.pi
    b = math.cos(a)
    main_window.txt_box.setText(str(b))


def tan():
    a = int(main_window.txt_box.text())
    a = a / 180 * math.pi
    b = math.tan(a)
    main_window.txt_box.setText(str(b))


def cot():
    a = int(main_window.txt_box.text())
    a = a / 180 * math.pi
    a = math.tan(a)
    b = 1 / a
    main_window.txt_box.setText(str(b))


def log():
    a = int(main_window.txt_box.text())
    b = math.log(a)
    main_window.txt_box.setText(str(b))


def result():
    b = int(main_window.txt_box.text())
    if operator == "sub":
        if percent == True:
            b = a * b / 100
            c = a - b
        else:
            c = a - b

    elif operator == "sum":
        if percent == True:
            b = a * b / 100
            c = a + b
        else:
            c = a + b

    elif operator == "div":
        if percent == True:
            b = a * b / 100
            c = a / b
        else:
            c = a / b

    elif operator == "mul":
        if percent == True:
            b = a * b / 100
            c = a * b
        else:
            c = a * b

    main_window.txt_box.setText(str(c))


def clear():
    main_window.txt_box.setText("")


app = QApplication([])

loader = QUiLoader()
main_window = loader.load("episode17\calculator_ui.ui")
main_window.show()

percent = False
main_window.btn_1.clicked.connect(number)
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_div.clicked.connect(div)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_perc.clicked.connect(perc)
main_window.btn_result.clicked.connect(result)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_log.clicked.connect(log)
main_window.btn_clear.clicked.connect(clear)


app.exec()
