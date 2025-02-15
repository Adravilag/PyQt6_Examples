# QGraphicsView/QGraphicsScene Examples in PyQt6

## Descripción

Este proyecto contiene tres ejemplos de uso de **QGraphicsView** y **QGraphicsScene** en PyQt6, cada uno con un nivel de complejidad creciente:

1. **Básico (`graphics_basic.py`):**
   - **Objetivo:**  
     Mostrar cómo agregar elementos gráficos simples (un rectángulo y una elipse) a una escena y visualizarlos mediante un QGraphicsView.
   - **Caso de Uso:**  
     Ideal para aplicaciones que requieran mostrar contenido gráfico estático o simples diagramas.

2. **Intermedio (`graphics_intermediate.py`):**
   - **Objetivo:**  
     Implementar un elemento gráfico personalizado (un triángulo) mediante la creación de una subclase de QGraphicsItem. El triángulo es seleccionable y movible.
   - **Caso de Uso:**  
     Útil para aplicaciones interactivas donde se necesite manipular o resaltar elementos gráficos de forma individual.

3. **Avanzado (`graphics_advanced.py`):**
   - **Objetivo:**  
     Crear una aplicación de dibujo interactivo donde el usuario pueda dibujar rectángulos en la escena mediante arrastrar y soltar el ratón.
   - **Caso de Uso:**  
     Aplicaciones de diseño gráfico, editores de diagramas o herramientas de anotación que permitan al usuario dibujar y modificar elementos en tiempo real.

## Requisitos

- **Python 3**
- **PyQt6**  
  Instala PyQt6 con:
  ```bash
  pip install PyQt6
