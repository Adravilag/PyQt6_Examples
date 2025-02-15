# QStandardItemModel Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran cómo utilizar **QStandardItemModel** en PyQt6 para gestionar y visualizar datos en una lista o vista similar. Cada ejemplo incrementa en complejidad y muestra distintas funcionalidades:

### Ejemplo 1: Básico (`standarditemmodel_basic.py`)
- **Objetivo:**  
  Crear un modelo básico basado en QStandardItemModel para mostrar una lista de cadenas en un QListView.
- **Caso de Uso:**  
  Ideal para aplicaciones simples que necesitan mostrar listas de información, como catálogos o menús.

### Ejemplo 2: Intermedio (`standarditemmodel_intermediate.py`)
- **Objetivo:**  
  Implementar un modelo editable basado en QStandardItemModel que permite modificar elementos directamente desde la vista.
- **Caso de Uso:**  
  Útil para aplicaciones de edición en línea, formularios o gestores de datos donde el usuario puede actualizar la información.

### Ejemplo 3: Avanzado (`standarditemmodel_advanced.py`)
- **Objetivo:**  
  Crear un modelo editable que soporte drag & drop para reordenar elementos en un QListView, con botones para agregar y eliminar ítems.
- **Caso de Uso:**  
  Aplicaciones que requieren una gestión interactiva de listas, como gestores de tareas o editores de configuraciones, permitiendo la personalización del orden y contenido.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
