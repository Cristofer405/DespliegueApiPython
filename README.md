# DespliegueApiPython

1. Creamos imagen de postgres en el contenedor de docker:
	docker pull postgres

2. Creamos un contendor de postgres:
	docker run --name my-collections -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres

3. Para crear la tabla ejecutamos:
	python create_table_db.py

4. Para desplegar el Dockerfile:
	docker build -t despliegueapi .

5. Para ejecutar la imagen creada:
	docker run --name my-despliegue-api -p 8080:8080 -d despliegue-api
