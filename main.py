from fastapi import FastAPI


from database import init_db
from routers import livros

# Cria a aplicação FastAPI
app = FastAPI(
    title="Sistema de Gestão de Livros",
    description="API REST para gerir livros",
    version="2.0.0",
    docs_url="/docs",  # Documentação Swagger
    redoc_url="/redoc"  # Documentação alternativa ReDoc
)

# Evento executado quando a aplicação inicia
@app.on_event("startup")
def startup():
    init_db()


# Regista o router de livros
# Todos os endpoints de livros ficam disponíveis
app.include_router(livros.router)

# Endpoint raiz (página inicial)
@app.get("/")
def raiz():
    """
    Endpoint inicial para verificar se a API está online.
    """
    return {
        "mensagem": "API de Gestão de Livros está online!",
        "versao": "2.0.0",
        "documentacao": {
            "swagger": "/docs",
            "redoc": "/redoc"
        },
        "endpoints": {
            "listar_livro": "GET /livros",
            "criar_livro": "POST /livros",
            "obter_livro": "GET /livros/{id}",
            "atualizar_livro": "PUT /livros/{id}",
            "apagar_livro": "DELETE /livros/{id}"
        }
    }

# Endpoint de saúde da API
@app.get("/health")
def health_check():
    """
    Verifica se a API está saudável e operacional.
    """
    return {"status": "ok", "mensagem": "API funcionando perfeitamente!"}