# media_player_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import Qt, QUrl

class IntermediateMediaPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QMediaPlayer Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Configurar la fuente de audio (asegúrate de que "test.mp3" exista)
        self.player.setSource(QUrl.fromLocalFile("test.mp3"))
        
        # Controles de reproducción
        controls_layout = QHBoxLayout()
        play_button = QPushButton("Play")
        pause_button = QPushButton("Pause")
        stop_button = QPushButton("Stop")
        controls_layout.addWidget(play_button)
        controls_layout.addWidget(pause_button)
        controls_layout.addWidget(stop_button)
        layout.addLayout(controls_layout)
        
        play_button.clicked.connect(self.player.play)
        pause_button.clicked.connect(self.player.pause)
        stop_button.clicked.connect(self.player.stop)
        
        # Control deslizante de volumen
        volume_layout = QHBoxLayout()
        volume_label = QLabel("Volume:")
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.audio_output.setVolume(0.5)
        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)
        layout.addLayout(volume_layout)
        
        self.volume_slider.valueChanged.connect(lambda v: self.audio_output.setVolume(v / 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateMediaPlayer()
    window.show()
    sys.exit(app.exec())
