# Advanced Text Editor with Shortcuts

## Descripción

Este proyecto es un editor de texto avanzado desarrollado con PyQt6 que incorpora una amplia variedad de atajos de teclado y herramientas integradas para mejorar la productividad del usuario. El editor permite realizar acciones comunes de edición de texto de manera rápida mediante atajos, y también ofrece una barra de herramientas y una barra de estado para brindar retroalimentación.

## Características

- **Interfaz Moderna:**  
  Basada en QMainWindow con un QTextEdit como widget central para la edición de texto.

- **Atajos de Teclado:**  
  - **Ctrl+N:** Crear un nuevo documento.
  - **Ctrl+O:** Abrir un archivo.
  - **Ctrl+S:** Guardar el documento actual.
  - **Ctrl+X:** Cortar texto.
  - **Ctrl+C:** Copiar texto.
  - **Ctrl+V:** Pegar texto.
  - **Ctrl+Z:** Deshacer acción.
  - **Ctrl+Y:** Rehacer acción.
  - **Ctrl+Q:** Cerrar la aplicación.

- **Barra de Herramientas:**  
  Acceso visual a las funciones más comunes, integradas con los atajos de teclado.

- **Barra de Estado:**  
  Muestra mensajes de confirmación para las operaciones realizadas (por ejemplo, "File saved successfully").

## ¿Cómo Funciona?

- **QShortcut y QKeySequence:**  
  Los atajos se definen utilizando QShortcut (importado desde PyQt6.QtGui) y QKeySequence.  
  Cada atajo está asociado a una acción específica del editor, permitiendo realizar tareas sin usar el ratón.

- **Acciones de Edición:**  
  El editor implementa funciones para crear nuevos documentos, abrir y guardar archivos, y editar el contenido (cortar, copiar, pegar, deshacer, rehacer).

## Caso de Uso Real

Este editor es útil para programadores, escritores o cualquier persona que necesite un entorno de edición de texto eficiente.  
El uso de atajos de teclado facilita la navegación y edición rápida, lo que es esencial en entornos de alta productividad.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Instala PyQt6 (si aún no lo tienes):
   ```bash
   pip install PyQt6
