# QSettings Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos de uso de **QSettings** en PyQt6, que ilustran distintas formas de almacenar y recuperar configuraciones de la aplicación:

1. **Básico (`qsettings_basic.py`):**
   - **Objetivo:**  
     Guardar y restaurar la geometría (tamaño y posición) de una ventana.
   - **Caso de Uso:**  
     Ideal para aplicaciones que necesiten recordar la posición y tamaño de la ventana entre sesiones.

2. **Intermedio (`qsettings_intermediate.py`):**
   - **Objetivo:**  
     Crear un formulario simple para que el usuario ingrese su nombre y edad, y guardar estos datos en QSettings.
   - **Caso de Uso:**  
     Útil para aplicaciones de configuración o formularios de usuario que requieran almacenar preferencias personales.

3. **Avanzado (`qsettings_advanced.py`):**
   - **Objetivo:**  
     Implementar un diálogo de configuración con múltiples pestañas usando QTabWidget, organizando la información en grupos (por ejemplo, "General" y "User"). Se utilizan grupos en QSettings para almacenar la configuración de manera estructurada.
   - **Caso de Uso:**  
     Aplicaciones complejas que requieren múltiples opciones de configuración organizadas de forma clara y persistente entre sesiones.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
