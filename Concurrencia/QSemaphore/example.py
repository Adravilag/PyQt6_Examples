import sys, time, random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar, QListWidget, QListWidgetItem
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt, QSemaphore

class WorkerSignals(QObject):
    finished = pyqtSignal(str)

class TaskWorker(QRunnable):
    """
    Worker que simula una tarea (por ejemplo, procesar un archivo).
    Utiliza QSemaphore para limitar la cantidad de tareas concurrentes.
    """
    def __init__(self, task_id, semaphore):
        super().__init__()
        self.task_id = task_id
        self.semaphore = semaphore
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        # Adquiere el semáforo: si se alcanzó el límite, se bloquea hasta que se libere
        self.semaphore.acquire()
        # Simula una tarea costosa (entre 1 y 2 segundos)
        time.sleep(random.uniform(1, 2))
        result = f"Task {self.task_id} finished."
        print(result)
        self.signals.finished.emit(result)
        # Libera el semáforo para permitir que otras tareas se ejecuten
        self.semaphore.release()

class QSemaphoreParallelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSemaphore Parallel Tasks - Improved")
        self.resize(500, 300)
        layout = QVBoxLayout(self)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        
        self.resultList = QListWidget(self)
        layout.addWidget(self.resultList)
        
        self.startButton = QPushButton("Start Tasks", self)
        layout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.start_tasks)
        
        # Configuramos el QThreadPool
        self.threadpool = QThreadPool()
        # Definimos el límite de tareas concurrentes (por ejemplo, 3)
        self.max_concurrent_tasks = 3
        self.semaphore = QSemaphore(self.max_concurrent_tasks)
        
        self.total_tasks = 6
        self.completed_tasks = 0
        self.results = []

    def start_tasks(self):
        self.resultList.clear()
        self.completed_tasks = 0
        self.results = []
        self.progressBar.setValue(0)
        
        for i in range(self.total_tasks):
            worker = TaskWorker(task_id=i+1, semaphore=self.semaphore)
            worker.signals.finished.connect(self.task_finished)
            self.threadpool.start(worker)
    
    @pyqtSlot(str)
    def task_finished(self, result):
        self.results.append(result)
        self.completed_tasks += 1
        progress = int((self.completed_tasks / self.total_tasks) * 100)
        self.progressBar.setValue(progress)
        self.resultList.addItem(QListWidgetItem(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSemaphoreParallelExample()
    window.show()
    sys.exit(app.exec())
