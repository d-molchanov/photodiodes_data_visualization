import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStyleFactory
)

from main_window import MainWindow
from main_widget import MainWidget
# from pdf_images_extractor_worker import PdfImagesExtractorWorker
# from pdf_images_extractor_widget import PdfImagesExtractorWidget


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.resize(800, 400)
    main_widget = MainWidget()
    # window.stop_worker.connect(main_widget.slot_stop_worker)
    window.setCentralWidget(main_widget)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
