from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    stop_worker = Signal()

    def __init__(self, parent=None, **kwargs) -> None:
        super().__init__(parent)

    def closeEvent(self, event):
        print('Main window is closing!')
        # self.stop_worker.emit()
        event.accept()