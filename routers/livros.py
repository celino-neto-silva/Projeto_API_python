"""
Define todos os endpoints (rotas) relacionados com livros.
Contém as operações CRUD (Create, Read, Update, Delete) conforme enunciado.
"""

from fastapi import APIRouter, HTTPException
from typing import List
import sqlite3
from database import get_db
from models import LivroCriar, LivroAtualizar, LivroResposta

# Cria um router para agrupar os endpoints de livros
router = APIRouter(
    prefix="/livros",  # Todos os endpoints começam com /livros
    tags=["Livros"]    # Agrupa na documentação
)

# ==================== GET /livros ====================


@router.get("", response_model=List[LivroResposta])
def listar_livros():
    """
    Retorna uma lista com todos os livros no catálogo.

    **Status de Sucesso:** 200 OK
    """
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM livros ORDER BY id")
        livros = [dict(row) for row in cursor.fetchall()]
        return livros


# ==================== GET /livros/{livro_id} ====================


@router.get("livros/{livro_id}", response_model=LivroResposta)
def obter_livro(livro_id: int):
    """
    Retorna os detalhes de um livro específico, identificado pelo seu ID único.

    **Status de Sucesso:** 200 OK
    **Status de Erro:** 404 Not Found se o livro não existir
    """
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        livro = cursor.fetchone()

        if livro is None:
            raise HTTPException(
                status_code=404,
                detail=f"Livro com ID {livro_id} não encontrado"
            )

        return dict(livro)

# ==================== POST /livros ====================


@router.post("", response_model=LivroResposta, status_code=201)
def criar_livro(livro: LivroCriar):
    """
    Adiciona um novo livro ao catálogo. Recebe os dados do livro no corpo da requisição.

    **Status de Sucesso:** 201 Created
    """
    with get_db() as conn:
        try:
            cursor = conn.execute(
                "INSERT INTO livros (isbn, titulo, autor, ano_publicacao) VALUES (?, ?, ?, ?)",
                (livro.isbn, livro.titulo, livro.autor, livro.ano_publicacao)
            )
            conn.commit()

            # Obtém o ID do livro criado
            livro_id = cursor.lastrowid
            return {**livro.dict(), "id": livro_id}

        except sqlite3.IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Erro ao criar livro: {str(e)}"
            )

# ==================== DELETE /livros/{livro_id} ====================


@router.delete("/{livro_id}", status_code=204)
def apagar_livro(livro_id: int):
    """
    Remove um livro do catálogo, identificado pelo seu ID único.

    **Status de Sucesso:** 204 No Content
    **Status de Erro:** 404 Not Found se o livro não existir
    """
    with get_db() as conn:
        cursor = conn.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Livro com ID {livro_id} não encontrado"
            )

        return {
            "mensagem": f"Livro com ID {livro_id} removido com sucesso",
            "sucesso": True
        }
# ==================== PUT /livros/{livro_id} ====================


@router.put("/{livro_id}", response_model=LivroResposta)
def atualizar_livro(livro_id: int, livro: LivroAtualizar):
    """
    Atualiza completamente um livro existente (DESAFIO OPCIONAL).

    **Status de Sucesso:** 200 OK
    **Status de Erro:** 404 Not Found se o livro não existir
    """
    with get_db() as conn:
        # Verifica se o livro existe
        cursor = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        if cursor.fetchone() is None:
            raise HTTPException(
                status_code=404,
                detail=f"Livro com ID {livro_id} não encontrado"
            )

        # Prepara os dados para atualização
        update_data = livro.dict(exclude_unset=True)
        if not update_data:
            raise HTTPException(
                status_code=400,
                detail="Nenhum campo fornecido para atualização"
            )

        # Constrói a query dinamicamente
        set_clause = ", ".join([f"{key} = ?" for key in update_data.keys()])
        values = list(update_data.values())
        values.append(livro_id)

        # Executa a atualização
        query = f"UPDATE livros SET {set_clause} WHERE id = ?"
        conn.execute(query, values)
        conn.commit()

        # Retorna o livro atualizado
        cursor = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
        return dict(cursor.fetchone())
