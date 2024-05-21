from pydantic import BaseModel

class Movies(BaseModel):
    id: int
    autor: str
    descripcion: str
    fecha_estreno: str

