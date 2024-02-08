# Gestión de Alquiler de Patinetes

Este proyecto consiste en una API REST desarrollada con Django para la gestión de una base de datos de alquiler de patinetes eléctricos.

## Información a guardar

### Patinete:
- Número
- Tipo
- Precio de desbloqueo
- Precio por minuto
- Estado de alquiler
  - Usuario
  - Fecha de desbloqueo
  - Fecha de entrega
  - Coste final

### Usuarios:
- Campo adicional: débito (con valor inicial 0)

## Requisitos del Ejercicio

1. Define los modelos correctamente.
2. Publica servicios para la gestión (CRUD) de los patinetes.
3. Publica servicios para que los usuarios puedan iniciar y terminar un alquiler:
   - Alquilar: Requiere autenticación del usuario e indicar un patinete libre.
   - Liberar: Requiere autenticación del usuario e indicar el patinete que se quiere liberar. Calculará el coste final y aumentará el débito del usuario.
4. Publica un servicio para el listado de todos los alquileres realizados visible solo para administradores.
5. Publica un servicio para el listado de los alquileres que solo pueda ver el usuario autenticado sobre sí mismo.

## Propuestas de Ampliación

1. Crear un servicio que muestre los patinetes libres.
2. Crear un servicio que muestre los patinetes ocupados.
3. Crear un servicio que devuelva los usuarios ordenados por débito.
4. Crear un servicio que devuelva el Top ten de patinetes alquilados.
5. Crear un servicio que devuelva el Top 3 de usuarios en número de alquileres realizados.
