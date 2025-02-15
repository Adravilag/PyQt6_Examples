# QScrollArea Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran distintas formas de utilizar **QScrollArea** en PyQt6 para gestionar contenido que excede el tamaño de la ventana, permitiendo el desplazamiento vertical y/o horizontal.

### Ejemplo 1: Básico (`scrollarea_basic.py`)
- **Objetivo:**  
  Mostrar un QScrollArea simple que contiene un QLabel con un texto extenso, de modo que se active el desplazamiento.
- **Caso de Uso:**  
  Ideal para visualizar contenido largo, como artículos o registros, dentro de un área de visualización limitada.

### Ejemplo 2: Intermedio (`scrollarea_intermediate.py`)
- **Objetivo:**  
  Utilizar QScrollArea para contener un conjunto de widgets organizados en un contenedor (QWidget) con un QVBoxLayout, lo que permite desplazar múltiples controles cuando exceden el tamaño de la ventana.
- **Caso de Uso:**  
  Útil para formularios o paneles de control que contengan múltiples elementos, donde se desea mantener una interfaz limpia mediante el desplazamiento.

### Ejemplo 3: Avanzado (`scrollarea_advanced.py`)
- **Objetivo:**  
  Implementar un QScrollArea con contenido dinámico. Un botón permite agregar nuevos elementos al contenedor, y el área de desplazamiento se actualiza para mostrar el nuevo contenido.
- **Caso de Uso:**  
  Aplicaciones que requieren cargar o agregar contenido de forma dinámica (por ejemplo, resultados de búsqueda, logs o mensajes en tiempo real) y mostrarlo en un área con desplazamiento.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
