# Appointment Scheduler

## Descripción

El proyecto "Appointment Scheduler" es una aplicación de escritorio desarrollada en PyQt6 que permite a los usuarios agendar citas.  
Utiliza **QCalendarWidget** para seleccionar fechas y un diálogo para ingresar detalles de la cita. Las citas se almacenan y se muestran en una lista, permitiendo ver las citas programadas para una fecha específica.

## Características

- **Selección de Fechas:**  
  Un QCalendarWidget interactivo permite al usuario seleccionar la fecha para la cual desea agendar una cita.

- **Agregar Citas:**  
  Al presionar el botón "Add Appointment", se abre un diálogo que muestra la fecha seleccionada y permite ingresar detalles de la cita.

- **Visualización de Citas:**  
  Las citas se almacenan internamente en un diccionario y se muestran en un QListWidget, mostrando todas las citas para la fecha seleccionada.

## Caso de Uso Real

Este sistema es útil para aplicaciones de agendamiento, tales como:
- Agendadores de citas médicas.
- Reservas de reuniones o espacios.
- Programación de eventos en centros de negocios o instituciones educativas.

La aplicación permite organizar y visualizar citas de manera intuitiva, mejorando la gestión del tiempo y la planificación.

## Cómo Usarlo

1. **Requisitos:**
   - Python 3
   - PyQt6

2. **Instalación:**
   Asegúrate de tener PyQt6 instalado:
   ```bash
   pip install PyQt6
