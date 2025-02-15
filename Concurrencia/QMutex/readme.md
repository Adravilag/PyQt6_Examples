# Bank Account Simulator with QMutex

## Descripción

Este proyecto simula un sistema bancario en el que múltiples hilos realizan operaciones de depósito y retiro sobre un saldo compartido.  
El acceso concurrente al saldo se protege mediante **QMutex** y **QMutexLocker** para asegurar que cada transacción se realice de forma atómica y sin interferencias.

## ¿Cómo Funciona?

- **QMutex y QMutexLocker:**  
  Cada hilo (tanto para depósitos como para retiros) utiliza un QMutexLocker para proteger la sección crítica donde se modifica el saldo global. Esto evita condiciones de carrera y garantiza la integridad de los datos.

- **Hilos de Depósito y Retiro:**  
  Se lanzan dos hilos:
  - **DepositThread:** Incrementa el saldo (simulando depósitos).
  - **WithdrawalThread:** Decrementa el saldo (simulando retiros), verificando que haya fondos suficientes.
  
- **Actualización Continua de la Interfaz:**  
  Se utiliza un QTimer que, cada 100 ms, actualiza la etiqueta que muestra el saldo. Esto asegura que la interfaz refleje en tiempo real los cambios realizados por los hilos, sin necesidad de intervención manual.

## Caso de Uso Real

En un sistema bancario real, múltiples transacciones pueden ocurrir de forma simultánea (depósitos, retiros, transferencias).  
El uso de QMutex asegura que estas transacciones se realicen de forma segura, evitando inconsistencias en el saldo.  
La actualización continua de la interfaz permite que el usuario vea el saldo actualizado en tiempo real.

## Cómo Usarlo

1. Asegúrate de tener Python 3 y PyQt6 instalados.
2. Ejecuta el script:
   ```bash
   python example.py