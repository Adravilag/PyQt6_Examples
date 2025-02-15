import sys, time, random
from PyQt6.QtCore import QThread, QMutex, QMutexLocker, pyqtSlot, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

# Saldo inicial de la cuenta
balance = 1000  
# QMutex para proteger el acceso al saldo compartido
mutex = QMutex()

class DepositThread(QThread):
    """Hilo que simula depósitos en la cuenta."""
    def __init__(self, amount, iterations, parent=None):
        super().__init__(parent)
        self.amount = amount
        self.iterations = iterations

    def run(self):
        global balance
        for _ in range(self.iterations):
            time.sleep(random.uniform(0.1, 0.3))
            with QMutexLocker(mutex):
                balance += self.amount
                print(f"Deposited ${self.amount}, new balance: ${balance}")

class WithdrawalThread(QThread):
    """Hilo que simula retiros de la cuenta."""
    def __init__(self, amount, iterations, parent=None):
        super().__init__(parent)
        self.amount = amount
        self.iterations = iterations

    def run(self):
        global balance
        for _ in range(self.iterations):
            time.sleep(random.uniform(0.1, 0.3))
            with QMutexLocker(mutex):
                if balance >= self.amount:
                    balance -= self.amount
                    print(f"Withdrew ${self.amount}, new balance: ${balance}")
                else:
                    print("Insufficient funds for withdrawal")

class BankSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Account Simulator with QMutex (Updated)")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.balance_label = QLabel(f"Balance: ${balance}", self)
        self.balance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.balance_label)
        
        self.start_button = QPushButton("Start Simulation", self)
        layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_simulation)
        
        # QTimer para actualizar la etiqueta del saldo continuamente
        self.timer = QTimer(self)
        self.timer.setInterval(100)  # Actualiza cada 100 ms
        self.timer.timeout.connect(self.update_balance)
        self.timer.start()

    @pyqtSlot()
    def start_simulation(self):
        global balance
        balance = 1000  # Reinicia el saldo a $1000
        self.start_button.setEnabled(False)
        # Crear hilos: uno para depósitos y otro para retiros
        self.deposit_thread = DepositThread(amount=50, iterations=20)
        self.withdraw_thread = WithdrawalThread(amount=30, iterations=20)
        self.deposit_thread.finished.connect(self.check_threads)
        self.withdraw_thread.finished.connect(self.check_threads)
        self.deposit_thread.start()
        self.withdraw_thread.start()

    @pyqtSlot()
    def update_balance(self):
        self.balance_label.setText(f"Balance: ${balance}")

    @pyqtSlot()
    def check_threads(self):
        if not self.deposit_thread.isRunning() and not self.withdraw_thread.isRunning():
            self.start_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BankSimulator()
    window.show()
    sys.exit(app.exec())
