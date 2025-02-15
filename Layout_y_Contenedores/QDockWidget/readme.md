# QDockWidget Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran distintas formas de utilizar **QDockWidget** en PyQt6, organizados en tres niveles de complejidad:

1. **Básico (`dockwidget_basic.py`):**
   - **Objetivo:** Mostrar un QDockWidget anclado en el área izquierda de un QMainWindow, con una lista simple.
   - **Caso de Uso:** Ideal para aplicaciones simples donde se requiere un panel lateral fijo, como un explorador de archivos.

2. **Intermedio (`dockwidget_intermediate.py`):**
   - **Objetivo:** Integrar múltiples QDockWidget en un QMainWindow, permitiendo que sean movibles, flotables y cerrables.
   - **Caso de Uso:** Útil en aplicaciones de escritorio donde se necesita organizar varios paneles (por ejemplo, un editor de código con paneles de navegación y de información).

3. **Avanzado (`dockwidget_advanced.py`):**
   - **Objetivo:** Permitir al usuario agregar y quitar dinámicamente dock widgets a través de un menú, personalizando la interfaz.
   - **Caso de Uso:** Aplicaciones altamente personalizables, donde el usuario puede configurar la disposición de la interfaz según sus necesidades (por ejemplo, entornos de desarrollo integrados).

## Requisitos

- Python 3
- PyQt6  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
