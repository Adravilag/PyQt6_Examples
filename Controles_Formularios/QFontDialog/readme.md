# QFontDialog Examples

## Descripción

Este proyecto presenta tres ejemplos de uso de **QFontDialog** en PyQt6, organizados por niveles de complejidad:

1. **Básico (font_dialog_basic.py):**  
   Permite al usuario seleccionar una fuente y aplicarla a un QLabel.  
   Ideal para comprender la funcionalidad fundamental de QFontDialog.

2. **Intermedio (font_dialog_intermediate.py):**  
   Muestra cómo aplicar la fuente seleccionada a múltiples widgets (un QLabel y un QLineEdit) de forma sincronizada.

3. **Avanzado (font_dialog_advanced.py):**  
   Simula un mini editor de estilos donde el usuario puede seleccionar una fuente, verla aplicada en una vista previa y "guardar" esa fuente para futuras aplicaciones.  
   Este ejemplo es útil en aplicaciones de edición de texto y diseño, donde se necesita una interfaz para personalizar estilos.

## ¿Cómo Funciona?

- **QFontDialog.getFont():**  
  Abre un diálogo de selección de fuente. Devuelve la fuente seleccionada y un valor booleano que indica si el usuario confirmó la elección.

- **Aplicación de la Fuente:**  
  En cada ejemplo, si el usuario confirma la selección, la fuente se aplica al widget correspondiente, actualizando la interfaz en tiempo real.

## Caso de Uso Real

- **Edición de Texto y Diseño:**  
  Permitir a los usuarios personalizar la apariencia de un documento o interfaz, eligiendo la fuente, el tamaño y otros atributos, lo que es esencial en editores de texto, herramientas de diseño y aplicaciones de presentación.

- **Aplicaciones Personalizadas:**  
  Un editor de estilos en aplicaciones gráficas que permita a los usuarios previsualizar y aplicar estilos personalizados a sus proyectos.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Instala PyQt6:
   ```bash
   pip install PyQt6
