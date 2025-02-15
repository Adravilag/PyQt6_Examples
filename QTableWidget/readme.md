# QTableWidget Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran diferentes formas de utilizar **QTableWidget** en PyQt6, con niveles de complejidad crecientes:

1. **Básico (`tablewidget_basic.py`):**
   - **Objetivo:**  
     Crear un QTableWidget con un número fijo de filas y columnas y poblarlo con datos estáticos.
   - **Caso de Uso:**  
     Ideal para aplicaciones que requieren mostrar información en una tabla de forma simple, como catálogos o menús.

2. **Intermedio (`tablewidget_intermediate.py`):**
   - **Objetivo:**  
     Implementar un QTableWidget editable en el que el usuario puede modificar los datos directamente. Se incluye un botón para mostrar el contenido de la tabla.
   - **Caso de Uso:**  
     Útil para formularios o aplicaciones de edición de datos donde se necesite actualizar la información en la tabla.

3. **Avanzado (`tablewidget_advanced.py`):**
   - **Objetivo:**  
     Permitir agregar y eliminar filas dinámicamente en un QTableWidget.  
   - **Caso de Uso:**  
     Aplicaciones que requieren gestionar datos que pueden cambiar en tiempo real, como gestores de tareas, inventarios o sistemas de registro.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
