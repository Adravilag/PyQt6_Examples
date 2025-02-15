# widget_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QMimeData, QUrl
from PyQt6.QtGui import QPixmap

class DragDropImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QWidget Example - Drag & Drop Image")
        self.resize(400, 300)

        self.setAcceptDrops(True)  # Habilitar la recepción de eventos de arrastre

        layout = QVBoxLayout(self)
        self.info_label = QLabel("Arrastra una imagen aquí", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio))
                self.info_label.setText(f"Imagen cargada: {file_path}")
            else:
                self.info_label.setText("El archivo no es una imagen válida")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropImageWidget()
    window.show()
    sys.exit(app.exec())
