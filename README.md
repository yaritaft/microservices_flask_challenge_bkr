# Ejercicio BKR

El ejercicio consiste de hacer una api con 2 tablas y armar endpoint REST para consultar,
crear, borrar o actualizar ambas tablas. Los servicios deben responder manejando solo el *Accept: application/json*

- [] Generar tablas `users` y `states`
- [] Importar informacion del archivo `stats.csv` en la tabla `states`
- [] Generar CRUD (REST) de `users`
- [] Generar endpoint (REST) `states`


## Tablas


### Users

Column | Type
------ | ----
id | int sequence ( PK )
name | string
age | int
state | int (FK states)
updated_at | datetime
created_at | datetime

### States
Column | Type
------ | ----
id | int sequence ( PK )
code | int
name | string
updated_at | datetime
created_at | datetime

### Author

### Pre requisites

### How to setup database

### How to load initial data

### How to run tests

### How to review the documentation

### How to run the app (2 Methods)

### How to consume the API

### Decisions made

### Standards applied
