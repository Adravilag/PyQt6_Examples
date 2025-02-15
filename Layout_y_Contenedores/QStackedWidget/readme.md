# QStackedWidget Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran distintas formas de utilizar **QStackedWidget** en PyQt6 para organizar interfaces mediante pestañas o páginas, con niveles de complejidad crecientes:

1. **Básico (`stackedwidget_basic.py`):**
   - **Objetivo:** Mostrar un QStackedWidget simple con dos páginas de contenido estático.
   - **Caso de Uso:** Ideal para aplicaciones sencillas que requieren cambiar entre dos o más vistas fijas, como un explorador de archivos o visor de documentos.

2. **Intermedio (`stackedwidget_intermediate.py`):**
   - **Objetivo:** Usar un QComboBox para cambiar entre páginas de un QStackedWidget, mostrando un formulario dividido en secciones (por ejemplo, Información Personal e Información de Contacto).
   - **Caso de Uso:** Útil para formularios o encuestas donde se desea agrupar la información en pestañas de forma lógica.

3. **Avanzado (`stackedwidget_advanced.py`):**
   - **Objetivo:** Permitir agregar y eliminar dinámicamente páginas (pestañas) en un QStackedWidget mediante botones de control.
   - **Caso de Uso:** Aplicaciones personalizables como editores de código o entornos de trabajo, donde el usuario puede agregar o quitar vistas según sus necesidades.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
