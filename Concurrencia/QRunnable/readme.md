# Concurrent File Processor

## Descripción

Este proyecto simula el procesamiento concurrente de archivos utilizando **QRunnable** y **QThreadPool** en PyQt6.  
En este ejemplo se genera una lista simulada de nombres de archivos y, para cada uno, se lanza un worker que procesa el archivo de forma concurrente.  
El procesamiento se simula mediante un retardo y la generación de un "recuento de palabras" aleatorio, y los resultados se muestran en una lista de la interfaz.

## ¿Cómo Funciona?

- **QRunnable:**  
  Cada archivo se procesa en un worker (implementado en la clase `FileProcessorWorker`) que hereda de QRunnable.  
  Este worker simula una tarea costosa (por ejemplo, procesamiento de imágenes, análisis de logs o datos de sensores) mediante un retardo.

- **QThreadPool:**  
  Los workers se encolan en un QThreadPool, permitiendo que múltiples tareas se ejecuten concurrentemente sin necesidad de gestionar manualmente cada hilo.

- **Señales:**  
  Cada worker emite una señal `finished` con el resultado del procesamiento, que se conecta a la función `update_results` de la interfaz para actualizar la lista de resultados.

## Caso de Uso Real

Este enfoque es útil en aplicaciones que necesitan procesar grandes volúmenes de archivos o datos de sensores en tiempo real, como:
- **Análisis de logs:** Procesar y extraer información relevante de múltiples archivos de registros.
- **Procesamiento de imágenes:** Aplicar filtros o análisis a un gran número de imágenes de forma concurrente.
- **Sistemas de monitoreo:** Recoger y procesar datos de múltiples sensores de manera simultánea para obtener estadísticas en tiempo real.

El uso de concurrencia con QThreadPool y QRunnable permite que la aplicación siga siendo responsiva, ya que las tareas pesadas se ejecutan en segundo plano sin bloquear la interfaz de usuario.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Asegúrate de tener PyQt6 instalado:
   ```bash
   pip install PyQt6
