# Ejemplos de QLineEdit con QCompleter en PyQt6

## Descripción General

Este proyecto contiene tres ejemplos que demuestran distintas implementaciones de autocompletado en un QLineEdit utilizando **QCompleter** en PyQt6. Cada ejemplo presenta un nivel de complejidad distinto y destaca características específicas para adaptar el autocompletado a diferentes necesidades:

1. **completer_basic.py:**  
   Ejemplo básico que utiliza un QLineEdit y QCompleter con una lista estática de palabras (por ejemplo, frutas). El autocompletado se activa a medida que el usuario escribe.

2. **complete_intermediate.py:**  
   Ejemplo intermedio que extiende QLineEdit (con la clase `TabCompleterLineEdit`) para que, al presionar la tecla Tab, se complete automáticamente la palabra actual con la sugerencia (la primera opción disponible del QCompleter).

3. **completer_advanced.py:**  
   Ejemplo avanzado que utiliza QCompleter con un modelo dinámico (QStringListModel) y un botón para "barajar" la lista de sugerencias. Esto simula un entorno en el que las sugerencias pueden cambiar dinámicamente, mostrando cómo actualizar el modelo del completador en tiempo real.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
