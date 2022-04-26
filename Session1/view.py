from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QHBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, name, id_):  # Overwrite, Override
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(600, 400)
        # Layout Management,
        widget = CentralWidget(name, id_)
        self.setCentralWidget(widget)


class CentralWidget(QWidget):
    def __init__(self, name, id_):
        super(CentralWidget, self).__init__()
        self.setStyleSheet("background:blue;")
        font = self.font()
        font.setPointSize(18)
        self.setFont(font)
        # Layout
        lay = QGridLayout()
        self.setLayout(lay)

        # Design
        lab = QLabel("Name")
        lay.addWidget(lab, 1, 1)
        lay.addWidget(QLabel("Id"), 2, 1)
        lay.addWidget(QLabel(name), 1, 2)
        lay.addWidget(QLabel(str(id_)), 2, 2)





