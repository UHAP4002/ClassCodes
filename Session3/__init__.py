import sys
from typing import List, Tuple

from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QWidget, QVBoxLayout, QTreeWidgetItem, QTableWidget, \
    QTableWidgetItem


class Students:
    def __init__(self):
        self.d = {}

    def add(self, name: str, id: str):
        self.d[id] = name

    def list(self) -> List[Tuple[str, str]]:
        return [(name, _id) for _id, name in self.d.items()]


class CentralWidget(QWidget):
    def __init__(self, students: Students):
        super(CentralWidget, self).__init__()
        lay = QVBoxLayout()
        self.setLayout(lay)
        tree = QTableWidget()
        tree.setRowCount(2)
        tree.setColumnCount(2)
        lay.addWidget(tree)
        for i, n in enumerate(students.list()):
            tree.setItem(i, 0, QTableWidgetItem(n[0]))
            tree.setItem(i, 1, QTableWidgetItem(n[1]))



class MainWindow(QMainWindow):
    def __init__(self, students: Students):
        super(MainWindow, self).__init__()
        self.setCentralWidget(CentralWidget(students))


if __name__ == '__main__':
    stu = Students()
    stu.add("Esmail", "70")
    stu.add("Asma", "80")
    app = QApplication([])
    man = MainWindow(stu)
    man.show()
    app.exec()
    sys.exit()


