# Hello there
from PyQt5.QtWidgets import QApplication
from model import Student
from view import MainWindow


# Test Data
stu = Student("Esmail", 973112569)

# End Test Data

app = QApplication([])
win = MainWindow(stu.name, stu.id)

win.show()
app.exec()  # Event Loop


