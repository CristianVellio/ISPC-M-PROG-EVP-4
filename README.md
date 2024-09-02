<h1>Modulo Programador 💻</h1>
<br>
<div>
    <img align="right" src="https://github.com/user-attachments/assets/8f2d463f-9f02-450e-af11-4c4d9a99a7d3" alt="AdobeColor-Portfolio" width="80" height="60">
<div>
<br><br><br>
  
<h2>Evidencia de Aprendizaje 4: "Diseño y Desarrollo de Objetos"</h2>

Instituto Superior Politecnico de Cordoba ISPC<br>
Docentes: Ivana Rojas Corsico; Martin Garlero<br>
Fecha de entrega: 08 de septiembre 2024<br>
Carrera: Desarrollo de Software<br>
Cohorte: 2024<br>
Alumno: Cristian Vellio<br>
Comision: 2<br>

<h2>Instrucciones</h2>
<h3>1. Selección y Diseño del Objeto:</h3>

○ Elige un objeto de los dos propuestos.<br>
○ Define 3 comportamientos clave del objeto que involucren lógica de
programación (no solo getters/setters).<br>
○ Incluye al menos un método estándar de definición def__.<br>

<h2>📱 Smartphone</h2>
Este proyecto implementa una clase Smartphone en Python que simula el comportamiento de un teléfono inteligente. La clase permite gestionar operaciones básicas como abrir y cerrar aplicaciones, instalar nuevas aplicaciones, y controlar el estado de la batería y el almacenamiento. Además, se hace uso de encapsulamiento para proteger los datos internos del objeto.

Características
Abrir y cerrar aplicaciones: Controla la apertura y cierre de aplicaciones y su impacto en la batería.
Gestión de almacenamiento: Instala y desinstala aplicaciones gestionando el espacio de almacenamiento disponible.<br>
Encapsulación: Usa atributos privados para asegurar la integridad de los datos.
Método __str__: Devuelve una representación en texto del estado del smartphone.



<h3>2. Desarrollo guiado por pruebas (TDD):</h3>
○ Escribe primero las pruebas unitarias.<br>
○ Implementa la clase para que pase las pruebas.<br>
○ Refactoriza en caso de ser necesario.<br>

<h2>🔎 Testing 🐞</h2>
Este proyecto incluye un conjunto de pruebas unitarias para asegurar que los métodos de la clase Smartphone funcionan correctamente. Las pruebas están implementadas usando el módulo unittest.

<h2>Instalacion y uso</h2>

1. Clona este repo.

```bash
git clone https://github.com/tu-usuario/smartphone-project.git
cd smartphone-project
```

2. Ejecuta las pruebas:

Para verificar que todo funcione correctamente, ejecuta las pruebas unitarias con:

```python 
py-m unittest test.py
```


<h3>3.Base de Datos</h3>

○ Diseña una base de datos que represente tu objeto.<br>
○ Escribe la sentencia CREATE TABLE, definiendo PK, FK, etc, según
corresponda.<br>
○ Crea 10 sentencias INSERT con datos de ejemplo.<br>
○ Escribe 5 consultas de tipo SELECT.<br>

<h2>🛢 Diseño de la Base de Datos 🛢</h2>
La base de datos contiene una tabla llamada `smartphones` que refleja las características principales de un smartphone. La estructura de la tabla es la siguiente:

- **id**: Identificador único de cada smartphone, configurado como clave primaria (PK).
- **marca**: Marca del smartphone, tipo de dato `VARCHAR`.
- **modelo**: Modelo del smartphone, tipo de dato `VARCHAR`.
- **bateria**: Nivel de batería del smartphone en porcentaje, tipo de dato `INT` con restricción de valores entre 0 y 100.
- **almacenamiento_total**: Capacidad total de almacenamiento en GB, tipo de dato `INT`.
- **almacenamiento_usado**: Espacio de almacenamiento usado en GB, tipo de dato `INT` con restricción para evitar valores negativos.
- **apps_abiertas**: Número de aplicaciones abiertas, tipo de dato `INT` con restricción para evitar valores negativos.

Sentencia `CREATE TABLE`

La sentencia SQL para crear la tabla `smartphones` es la siguiente:

```sql
CREATE TABLE smartphones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    bateria INT CHECK (bateria BETWEEN 0 AND 100),
    almacenamiento_total INT NOT NULL,
    almacenamiento_usado INT NOT NULL CHECK (almacenamiento_usado >= 0),
    apps_abiertas INT NOT NULL CHECK (apps_abiertas >= 0)
);
```
Se insertaron 10 registros de ejemplo en la tabla smartphones para ilustrar el uso de la base de datos. Aquí algunos ejemplos

```sql
INSERT INTO smartphones (marca, modelo, bateria, almacenamiento_total, almacenamiento_usado, apps_abiertas)
VALUES ('Voltron', 'X_20z223', 90, 128, 20, 1);

INSERT INTO smartphones (marca, modelo, bateria, almacenamiento_total, almacenamiento_usado, apps_abiertas)
VALUES ('Voltron', 'Y_15b64', 75, 256, 50, 2);

-- [...]
```
Y se presentan 5 consultas SELECT diseñadas para interactuar con la tabla smartphones:
<div>
<img src="https://github.com/user-attachments/assets/1830ce48-ab90-4a06-b1cc-c47ed7f98e98" alt="Query-Select-1" width="250" height="100">
<img src="https://github.com/user-attachments/assets/f1952143-aa96-4438-b38c-dd0602c1c3ad" alt="Query-Select-2" width="250" height="100">
<img src="https://github.com/user-attachments/assets/81a261cf-7e06-49ff-808d-a4dd22fb130e" alt="Query-Select-3" width="250" height="100">
<img src="https://github.com/user-attachments/assets/e8924854-0e62-40a2-bcfe-79cad2521c45" alt="Query-Select-4" width="250" height="100">
<img src="https://github.com/user-attachments/assets/bdd674b7-9377-4518-b522-9bc9f6a331b6" alt="Query-Select-5" width="250" height="100">


</div>

<div align="center">
    <img src="https://github.com/user-attachments/assets/54097fd9-6010-4ca2-ae38-8b3cebd59b95" alt="Query-All" width="500" height="200">
</div>

<h2>Link DEMO YT</h2>
<br>
<br>
<br>
<div align="center">
  <a href="https://youtu.be/mIxR4VrStX4?feature=shared">Evidencia 4 Demo</a>
</div>
<br>
<br>
<br>


## **Stack Tecnológico**
Back-End:
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"  width="20" height="20"/> Python
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" width="20" height="20"/> MySQL
