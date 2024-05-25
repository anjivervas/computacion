# Registro y Visualización de Datos

> Este programa permite gestionar las notas. Se compone de tres archivos que trabajan en conjunto para ofrecer diversas funcionalidades:

## 1. uno.py :

> Archivo principal que contiene las importaciones necesarias. 

Define las funciones del menú y controlando la interacción del usuario. Además, evalúa las opciones seleccionadas y llama a las funciones correspondientes.

## 2. dos.py :

Contiene las funciones específicas para cada operación del programa como:

* Nombre: Busca el nombre del estudiante a partir de su número de cédula.

* Apellido: Busca el apellido del estudiante a partir de su número de cédula.

* Periodos: Obtiene los periodos en los que un estudiante ha cursado materias.

* Promedio: Calcula el promedio general de un estudiante, considerando todas sus notas y unidades de crédito.

* Agregar estudiante: Permite agregar un nuevo estudiante a la base de datos.

* Eliminar estudiante: Elimina un estudiante existente de la base de datos, junto con todas sus notas.

## 3. cuatro.json :

> Archivo JSON que sirve como base de datos del programa.

Almacena la información de los estudiantes, materias y notas en una estructura de datos organizada.

Cada registro incluye información como el número de cédula, nombre, apellido, código de materia, nota, periodo y unidades de crédito.