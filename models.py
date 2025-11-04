from pydantic import BaseModel
from typing import Optional

class Livro(BaseModel):
    id: Optional[int]
    titulo: str
    autor: str
    ano_publicacao: int