# Order Processing Simulator with QThreadPool

## Descripción

Este proyecto simula el procesamiento concurrente de pedidos en una tienda en línea utilizando **QThreadPool** y **QRunnable** en PyQt6. Cada pedido se procesa en paralelo, lo que permite que la aplicación mantenga una interfaz responsiva incluso cuando se realizan tareas intensivas en segundo plano.

## ¿Cómo Funciona?

- **QThreadPool y QRunnable:**
  - **QRunnable:** Cada pedido se procesa en un worker (`OrderWorker`) que hereda de QRunnable. Este worker simula el procesamiento de un pedido (por ejemplo, verificando inventario, calculando precios o comunicándose con un sistema de pago) mediante un retardo aleatorio.
  - **QThreadPool:** Los workers se encolan en un QThreadPool, permitiendo la ejecución concurrente de múltiples tareas sin la necesidad de gestionar manualmente cada hilo.

- **Comunicación mediante Señales:**
  - Cada `OrderWorker` emite la señal `finished` con el resultado del procesamiento cuando finaliza.
  - La interfaz principal recibe estas señales y actualiza una lista (QListWidget) con los resultados de cada pedido.

## Caso de Uso Real

En una aplicación de comercio electrónico, los pedidos pueden ser procesados simultáneamente para optimizar el rendimiento y reducir el tiempo de espera del usuario.  
Por ejemplo, cuando un cliente realiza un pedido, el sistema podría:
- Validar el pedido.
- Consultar el inventario.
- Procesar el pago.
- Actualizar el estado del pedido.

El uso de QThreadPool y QRunnable permite ejecutar estas operaciones en segundo plano sin bloquear la interfaz de usuario, garantizando una experiencia fluida y eficiente.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Asegúrate de tener PyQt6 instalado:
   ```bash
   pip install PyQt6
