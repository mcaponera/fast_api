# fast zer0

### banco de dados
- `models.py`:
recebe os modelos do banco de dados, modelamos nosso banco usando o `registry` do `sqlalchemy`. com o `registry` registramos os metadados referentes ao campo das tabela, nesse caso usamos as dataclasses do python para mapear nossa tabela (mapped relational object), criando um objeto escalar. o atributo `mapped_column` do `sqlalchemy` para mapear as constraints da tabela, como `pk`, `unique`
- `engine`:
```python
    # gerenciamento de contexto live 43
    with Session(engine) as session:
        # transforma uma função em um gerador playlist introdução a corrotinas live 51
        yield session
```
- `relationship`:
define como as tabelas interagem, o argumento `back-populates` permite a associação bidirecional, ou seja acessar o usuário pelas tarefas e o contário, o argumento `cascade` define o que acontece com as tarefa qndo o usuário é deletado.