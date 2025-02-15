# Order Processing Simulator

## Descripción
Este proyecto simula el procesamiento concurrente de pedidos en una tienda en línea utilizando **QThread** en PyQt6.  
Cada pedido se procesa en un hilo independiente, lo que permite que múltiples pedidos se gestionen de forma simultánea sin bloquear la interfaz de usuario.

## ¿Cómo Funciona?
- **QThread:**  
  Se crea una instancia de `OrderProcessor` para cada pedido.  
  Cada hilo simula el procesamiento de un pedido (con un retardo aleatorio entre 1 y 3 segundos) y emite una señal cuando finaliza.

- **Comunicación:**  
  La señal `orderProcessed` es conectada al método `display_result` del widget principal, que actualiza la interfaz (un QListWidget) con el resultado de cada pedido.

## Caso de Uso Real
En un sistema de procesamiento de pedidos real, cada pedido puede requerir operaciones intensivas (verificación de stock, cálculo de precios, etc.).  
Usar QThread permite que cada pedido se procese en paralelo, lo que mejora la eficiencia y mantiene la interfaz responsiva.

## Cómo Usarlo
1. Asegúrate de tener Python 3 y PyQt6 instalados.
2. Ejecuta el script:
   ```bash
   python order_processing.py
