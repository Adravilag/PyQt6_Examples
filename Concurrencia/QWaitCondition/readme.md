# Sensor Data Queue Simulator (QWaitCondition)

## Descripción
Este proyecto simula un sistema de monitoreo de sensores en el que múltiples hilos productores generan datos de sensores y un hilo consumidor procesa estos datos de forma concurrente.  
La sincronización entre productores y consumidor se logra utilizando **QMutex** y **QWaitCondition** para garantizar que el consumidor se bloquee hasta que haya datos disponibles en la cola compartida.

## ¿Cómo Funciona?
- **Productores (SensorProducer):**
  - Simulan la lectura de datos de sensores (por ejemplo, temperaturas) a intervalos aleatorios.
  - Cada productor añade sus datos a una cola compartida protegida por un mutex.
  - Tras agregar un dato, el productor despierta al consumidor mediante `condition.wakeAll()`.

- **Consumidor (SensorConsumer):**
  - Espera a que haya datos disponibles en la cola. Si la cola está vacía, se bloquea usando `condition.wait(mutex)`.
  - Una vez que se dispone de datos, los extrae de la cola y simula su procesamiento.
  - Emite una señal para notificar la operación consumida.

- **Sincronización:**
  - **QMutex** protege el acceso a la cola compartida (`sensor_queue`).
  - **QWaitCondition** permite que el consumidor se bloquee hasta que los productores añadan nuevos datos.

## Caso de Uso Real
Este patrón es común en sistemas IoT o en entornos industriales donde:
- Múltiples sensores envían datos de forma concurrente.
- Un sistema central (o un hilo consumidor) procesa estos datos en tiempo real para generar alertas, estadísticas o almacenar información.
El uso de QWaitCondition y QMutex asegura que el procesamiento se realice de forma ordenada, evitando condiciones de carrera y garantizando la integridad de los datos.

## Cómo Usarlo
1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Ejecución:**
   - Guarda el script `sensor_data_queue.py` en tu directorio de trabajo.
   - Ejecuta el script:
     ```bash
     python sensor_data_queue.py
     ```
3. **Uso:**
   - Presiona el botón "Start Simulation" para iniciar la generación y el procesamiento de datos.
   - La interfaz mostrará un registro en tiempo real de los datos producidos y consumidos en un QListWidget.
   - Consulta la consola para ver mensajes adicionales de producción y consumo.

## Requisitos
- Python 3
- PyQt6

