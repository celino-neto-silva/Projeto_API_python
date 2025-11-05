from pydantic import BaseModel,Field

class LivroBase(BaseModel):
    isbn: str = Field(None, title="ISBN", description="Código ISBN do livro")
    titulo: str = Field( title="Título do Livro", description="Nome completo do livro", min_length=3)
    autor: str = Field( title="Autor", description="Nome completo do autor")
    ano_publicacao: int = Field( ge=1900, le=2025, description="Ano em que o livro foi publicado")


class LivroCriar(LivroBase):
    pass

class LivroAtualizar(LivroBase):
    pass

class LivroResposta(LivroBase):
    pass
    class Config:

        from_attributes = True
