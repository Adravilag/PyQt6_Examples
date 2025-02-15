# QStyledItemDelegate Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran cómo utilizar **QStyledItemDelegate** en PyQt6 para personalizar la apariencia y la edición de elementos en vistas:

1. **Básico (`styled_delegate_basic.py`):**  
   - **Objetivo:**  
     Utilizar un delegado personalizado para cambiar la apariencia de los elementos en un QListView.  
   - **Caso de Uso:**  
     Ideal para resaltar elementos (por ejemplo, cambiar el color de texto cuando se selecciona un elemento).

2. **Intermedio (`styled_delegate_intermediate.py`):**  
   - **Objetivo:**  
     Implementar un delegado que modifica el formato de los elementos (por ejemplo, usar una fuente en negrita para la primera columna) en un QTableView con un modelo editable.  
   - **Caso de Uso:**  
     Útil en aplicaciones de edición o visualización de datos donde se requiere resaltar o diferenciar información.

3. **Avanzado (`styled_delegate_advanced.py`):**  
   - **Objetivo:**  
     Crear un delegado que proporciona un editor personalizado (un QComboBox) para una columna de un QTableView.  
   - **Caso de Uso:**  
     Aplicaciones que requieren selección de opciones predefinidas al editar celdas, como en un formulario o configurador de opciones.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
