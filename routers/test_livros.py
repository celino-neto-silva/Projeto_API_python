import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestListarLivros(unittest.TestCase):
    def setUp(self):
        self.livros_dummy = [
            {"id": 1, "titulo": "Livro 1", "autor": "Autor 1", "ano_publicacao": 2020},
            {"id": 2, "titulo": "Livro 2", "autor": "Autor 2", "ano_publicacao": 2021},
            {"id": 3, "titulo": "Livro 3", "autor": "Autor 3", "ano_publicacao": 2022},
            {"id": 4, "titulo": "Livro 4", "autor": "Autor 4", "ano_publicacao": 2023}
        ]

    def test_listar_livros(self):
        response = client.get("/livros")
        assert response.status_code == 200
        assert response.json() == self.livros_dummy

    # ... rest of the test functions ...


class TestObterLivro(unittest.TestCase):
    def setUp(self):
        self.livros_dummy = [
            {"id": 1, "titulo": "Livro 1", "autor": "Autor 1", "ano_publicacao": 2020},
            {"id": 2, "titulo": "Livro 2", "autor": "Autor 2", "ano_publicacao": 2021},
            {"id": 3, "titulo": "Livro 3", "autor": "Autor 3", "ano_publicacao": 2022},
            {"id": 4, "titulo": "Livro 4", "autor": "Autor 4", "ano_publicacao": 2023}
        ]

    def test_obter_livro(self):
        for livro in self.livros_dummy:
            response = client.get(f"/livros/{livro['id']}")
            assert response.status_code == 200
            assert response.json() == livro

    # ... rest of the test functions ...


class TestCriarLivro(unittest.TestCase):
    def setUp(self):
        self.livros_dummy = [
            {"id": 1, "titulo": "Livro 1", "autor": "Autor 1", "ano_publicacao": 2020},
            {"id": 2, "titulo": "Livro 2", "autor": "Autor 2", "ano_publicacao": 2021},
            {"id": 3, "titulo": "Livro 3", "autor": "Autor 3", "ano_publicacao": 2022},
            {"id": 4, "titulo": "Livro 4", "autor": "Autor 4", "ano_publicacao": 2023}
        ]

    def test_criar_livro(self):
        novo_livro = {"id": 5, "titulo": "Livro 5",
                      "autor": "Autor 5", "ano_publicacao": 2024}
        response = client.post("/livros", json=novo_livro)
        assert response.status_code == 201
        assert response.json()["id"] == 5
        assert response.json()["titulo"] == "Livro 5"
        assert response.json()["autor"] == "Autor 5"
        assert response.json()["ano_publicacao"] == 2024

    # ... rest of the test functions ...


if __name__ == "__main__":
    unittest.main()
