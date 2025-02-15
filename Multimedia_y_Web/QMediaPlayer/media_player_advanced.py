import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl

class AdvancedMediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QMediaPlayer Example")
        self.resize(800, 600)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Layout principal con estiramiento para el área de video
        main_layout = QVBoxLayout(central_widget)
        
        # Widget de video: ocupará la mayor parte del espacio
        self.video_widget = QVideoWidget()
        main_layout.addWidget(self.video_widget, stretch=8)  # mayor peso
        
        # Configuración del reproductor
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self.video_widget)
        # Asegúrate de tener un archivo de video llamado "sample_video.mp4" o cambia la ruta
        self.player.setSource(QUrl.fromLocalFile("videos/sample_video.mp4"))
        
        # Controles: se ubican en la parte inferior con menor estiramiento
        controls_layout = QHBoxLayout()
        
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.pause_button)
        controls_layout.addWidget(self.stop_button)
        
        self.play_button.clicked.connect(self.player.play)
        self.pause_button.clicked.connect(self.player.pause)
        self.stop_button.clicked.connect(self.player.stop)
        
        # Slider para posición de reproducción
        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 0)
        
        # Etiqueta para tiempo de reproducción
        self.time_label = QLabel("00:00 / 00:00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Agregar controles y slider en un layout adicional
        bottom_layout = QVBoxLayout()
        bottom_layout.addLayout(controls_layout)
        bottom_layout.addWidget(self.position_slider)
        bottom_layout.addWidget(self.time_label)
        
        # Agregar el layout de controles al layout principal con menor estiramiento
        main_layout.addLayout(bottom_layout, stretch=2)
        
        # Conectar señales para actualizar slider y tiempo
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.position_slider.sliderMoved.connect(self.player.setPosition)

    def position_changed(self, position):
        self.position_slider.setValue(position)
        self.update_time_label(position, self.player.duration())
        
    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)
        
    def update_time_label(self, position, duration):
        def ms_to_time(ms):
            seconds = ms // 1000
            minutes = seconds // 60
            seconds = seconds % 60
            return f"{minutes:02}:{seconds:02}"
        self.time_label.setText(f"{ms_to_time(position)} / {ms_to_time(duration)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedMediaPlayer()
    window.show()
    sys.exit(app.exec())
