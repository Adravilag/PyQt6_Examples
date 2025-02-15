# QWidget Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos que demuestran diferentes formas de utilizar **QWidget** en PyQt6, con niveles de complejidad creciente:

1. **Básico (`widget_basic.py`):**
   - **Objetivo:** Mostrar un `QWidget` con un layout simple que contiene un `QLabel` y un `QPushButton`.  
   - **Caso de Uso:** Ideal para ventanas simples o diálogos básicos con controles lineales.

2. **Intermedio (`widget_intermediate.py`):**
   - **Objetivo:** Implementar un `QWidget` que maneje eventos de ratón y dibuje un rectángulo con un **QPainter**.  
   - **Caso de Uso:** Aplicaciones interactivas donde el usuario necesite dibujar o manipular gráficos (por ejemplo, un editor de diagramas).

3. **Avanzado (`widget_advanced.py`):**
   - **Objetivo:** Crear un `QWidget` que soporte drag & drop de imágenes, mostrando la imagen arrastrada dentro del widget.  
   - **Caso de Uso:** Aplicaciones que requieran arrastrar archivos o imágenes desde el sistema operativo, como editores de imágenes, gestores de contenido, etc.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
