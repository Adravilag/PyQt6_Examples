# media_player_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

class BasicMediaPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QMediaPlayer Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Configurar la fuente de audio (asegúrate de que "test.mp3" exista)
        self.player.setSource(QUrl.fromLocalFile("test.mp3"))
        
        play_button = QPushButton("Play", self)
        play_button.clicked.connect(self.player.play)
        layout.addWidget(play_button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMediaPlayer()
    window.show()
    sys.exit(app.exec())
