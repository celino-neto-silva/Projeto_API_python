from pydantic import BaseModel
#from typing import Optional

class LivroBase(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int


class LivroCriar(LivroBase):
    pass

class LivroAtualizar(LivroBase):
    pass

class LivroResposta(LivroBase):
    pass
    class Config:
        from_attributes = True