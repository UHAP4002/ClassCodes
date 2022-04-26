from typing import Callable

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, \
    QPushButton, QVBoxLayout

from x import Students


class MainWindow(QMainWindow):
    def __init__(self, db, add):
        super().__init__()

        self.setWindowTitle("Students")
        self.setGeometry(100, 100, 450, 500)

        self.setCentralWidget(MainWidget(db, add))
        self.show()


class MainWidget(QWidget):
    def __init__(self, db: Students, add: Callable[[str, str], None]):
        super().__init__()
        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(StudentsView(db))
        lay.addWidget(AddStudent(add))


class StudentsView(QWidget):
    def __init__(self, db: Students):
        super(StudentsView, self).__init__()
        std = db.list()
        std_len = len(std)
        layout = QHBoxLayout()
        self.setLayout(layout)
        std_table = QTableWidget(std_len, 2)
        std_table.setHorizontalHeaderLabels(["Name", "Id"])

        for idx, (name, id) in enumerate(std):
            std_table.setItem(idx, 0, QTableWidgetItem(name))
            std_table.setItem(idx, 1, QTableWidgetItem(id))

        layout.addWidget(std_table)


class AddStudent(QWidget):
    def __init__(self, add):
        super(AddStudent, self).__init__()
        self.add = add
        lay = QVBoxLayout()
        self.setLayout(lay)
        name = QLineEdit()
        self.name = name
        lay.addWidget(name)
        _id = QLineEdit()
        self._id = _id
        lay.addWidget(_id)
        btn = QPushButton("Add")
        btn.pressed.connect(self.btn_press)
        lay.addWidget(btn)

    def btn_press(self):
        _id = self._id.text()
        name = self.name.text()
        self.add(_id, name)


if __name__ == "__main__":
    s = Students()
    s.add("ali", "1")
    s.add("reza", "2")

    app = QApplication([])
    window = MainWindow(s, s.add)
    app.exec()