# QSemaphore Parallel Tasks - Improved

## Descripción

Este proyecto simula el procesamiento concurrente de tareas utilizando **QSemaphore** para limitar la cantidad de tareas que se ejecutan en paralelo.  
En este ejemplo se encolan 6 tareas (simulando, por ejemplo, el procesamiento de archivos o solicitudes) y se utiliza un QSemaphore para permitir solo 3 tareas concurrentes a la vez.  
Cada tarea tarda entre 1 y 2 segundos en completarse y, al finalizar, se actualiza una barra de progreso y se muestran los resultados en una lista.

## ¿Cómo Funciona?

- **QSemaphore:**  
  Limita la concurrencia a un número fijo de tareas (en este caso, 3). Cada worker debe adquirir el semáforo antes de comenzar y liberarlo al finalizar.

- **QRunnable y QThreadPool:**  
  Se utilizan para ejecutar las tareas concurrentemente sin bloquear la interfaz.  
  Cada tarea se implementa en la clase `TaskWorker` que hereda de QRunnable.

- **Actualización de la Interfaz:**  
  A medida que cada tarea finaliza, se actualiza una barra de progreso y se añaden resultados a una lista.

## Caso de Uso Real

Este enfoque es útil en aplicaciones que necesitan procesar múltiples archivos o solicitudes de manera concurrente sin sobrecargar el sistema.  
Por ejemplo, en una aplicación de procesamiento de imágenes, podrías limitar el número de imágenes que se procesan simultáneamente para evitar el uso excesivo de recursos, manteniendo la aplicación responsiva y eficiente.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Asegúrate de tener PyQt6 instalado:
   ```bash
   pip install PyQt6
