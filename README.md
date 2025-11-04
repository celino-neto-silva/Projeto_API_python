#Projeto em grupo – API para livros
-----------------------------------

Descrição: O presente projeto tem como objetivo a constituição de uma API para a gestão de livros.

#Requisitos Funcionais (“Funcionalidades que deve ter”):
-	Método GET para mostrar lista de livros
-	Método GET para mostrar livro específico
-	Método POST para cadastrar um novo livro
-	Método DELETE para remover um livro
-	Método PUT para atualizar um livro

#Restrições:
-	Modelo livro com os atributos:
1.	ID (“ISBN”)
2.	Título
3.	Autor
4.	Ano de publicação
-	Comprimento mínimo de título = 3 caracteres
-	Comprimento mínimo de autor = 3 caracteres
-	Ano de publicação entre 1900 e o ano atual

#Tratamento de erros:
-O endpoint GET e DELETE por ID devem retornar o código de status 404 Not Found se o livro com o ID fornecido não existir
-O endpoint POST deve verificar se o ID fornecido já existe e retornar um 400 Bad Request caso haja duplicidade
