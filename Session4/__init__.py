import time

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QProgressBar, QApplication


class MyThread(QThread):
    new_value = pyqtSignal("PyQt_PyObject")

    def run(self) -> None:
        for i in range(100):
            time.sleep(0.3)
            # noinspection PyUnresolvedReferences
            self.new_value.emit(i)


app = QApplication([])
x = QProgressBar()
y = QProgressBar()
y.show()

x.setMinimum(0)
x.setMaximum(100)
# x.setValue(50)
x.show()
m = MyThread()
m.start()
m.new_value.connect(lambda e: x.setValue(e))


# def set_value():
#     global a
#     a += 1
#     x.setValue(a)


# timer = QTimer()
# timer.setInterval(500)
# timer.timeout.connect(set_value)
# timer.start()
app.exec()
print("hello")

# progress_bar.setValue(i)



