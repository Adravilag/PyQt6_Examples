# QAbstractListModel Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos de uso de **QAbstractListModel** en PyQt6, cada uno con un nivel de complejidad creciente, que muestran cómo implementar modelos personalizados para alimentar vistas en PyQt6.

### Ejemplo 1: Básico (`listmodel_basic.py`)
- **Objetivo:**  
  Crear un modelo simple basado en QAbstractListModel para mostrar una lista de cadenas (por ejemplo, nombres de frutas).
- **Caso de Uso:**  
  Ideal para aplicaciones que requieren mostrar listas de texto en vistas como QListView.

### Ejemplo 2: Intermedio (`listmodel_intermediate.py`)
- **Objetivo:**  
  Extender QAbstractListModel para incluir roles personalizados. En este ejemplo, cada elemento es un diccionario que contiene un nombre y un color. Se utiliza un rol personalizado para acceder al color.
- **Caso de Uso:**  
  Útil en aplicaciones donde se requiere asociar múltiples datos a cada elemento (por ejemplo, mostrar una lista de productos con sus atributos).

### Ejemplo 3: Avanzado (`listmodel_advanced.py`)
- **Objetivo:**  
  Implementar un modelo editable basado en QAbstractListModel. El usuario puede modificar directamente los elementos de la lista y también agregar o eliminar ítems.
- **Caso de Uso:**  
  Ideal para aplicaciones que requieren edición en línea de listas, como gestores de tareas, editores de configuraciones o cualquier sistema interactivo de gestión de datos.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
