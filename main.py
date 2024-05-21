from fastapi import FastAPI, HTTPException, status
from models import Movies
from connection import Coneccion as cn

app = FastAPI()


@app.get('/pelicula')
def get_pelicula():

    list_tmp = []

    with cn.cursor() as cursor:
        
        try:
            query = '''
            SELECT * FROM my_movies
            '''
            
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
                list_tmp.append(row)
        except:
            print("Error con la consulta GET")

    return {"message": list_tmp}


@app.get('/pelicula/{idM}')
def get_single_pelicula(idM: int):

    list_tmp = []

    with cn.cursor() as cursor:
        
        try:
            query = f'''
            SELECT * FROM my_movies WHERE id = %s;
            '''
            data = (idM,)
            cursor.execute(query, data)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
                list_tmp.append(rows)
        except:
            print("Error con la consulta GET")

    return {"message": list_tmp}


@app.post('/pelicula')
def create_pelicula(eMovies: Movies):

    with cn.cursor() as cursor:
        
        if eMovies.autor.strip() == "":
            return {"message": "Debe ingresar datos del autor."}
        
        if eMovies.descripcion.strip() == "":
            return {"message": "Debe ingresar datos de la descripción."}
        
        if eMovies.fecha_estreno.strip() == "":
            return {"message": "Debe ingresar datos de la fecha de estreno."}
        
        try:
            query = f'''
            INSERT INTO my_movies (autor, descripcion, fecha_estreno) VALUES (%s, %s, %s);
            '''

            data = (eMovies.autor, eMovies.descripcion, eMovies.fecha_estreno)
            cursor.execute(query, data )
            cn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta POST")

    return {"message": "Creado correctamente"}


@app.put('/pelicula')
def update_pelicula(eMovies: Movies):

    with cn.cursor() as cursor:
        vAutor = eMovies.autor

        try:
            query = f'''
            UPDATE my_movies SET autor = %s, descripcion = %s, fecha_estreno = %s WHERE id = %s;
            '''

            data = (eMovies.autor, eMovies.descripcion, eMovies.fecha_estreno, eMovies.id)
            cursor.execute(query, data )
            cn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta PUT")

    return {"message": "Actualizado correctamente"}


@app.delete('/pelicula')
def update_pelicula(eMovies: Movies):

    with cn.cursor() as cursor:
        
        try:
            query = f'''
            DELETE FROM my_movies WHERE id = %s;
            '''

            data = (eMovies.id,)
            cursor.execute(query, data )
            cn.commit()

        except Exception as e:
            print(e)
            print("Error con la consulta DELETE")

    return {"message": "Borrado correctamente"}
