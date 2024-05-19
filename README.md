# DespliegueApiPython

1. Creamos imagen de postgres en el contenedor de docker:
   docker pull postgres

3. Creamos un contendor de postgres:
   docker run --name my-collections -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres

5. Para crear la tabla ejecutamos:
   python create_table_db.py

7. Para desplegar el Dockerfile:
   docker build -t despliegueapi .

9. Para ejecutar la imagen creada:
   docker run --name my-despliegue-api -p 8080:8080 -d despliegue-api
