# Desafio de Testes Unitários com Pytest

Projeto desenvolvido para praticar validações de formato e o uso do framework **pytest**.

A classe `Validador`, localizada em `validador.py`, possui métodos para validação de:

- CPF
- CNPJ
- CEP

Os testes estão localizados em `test/test_validador.py` e utilizam `pytest.fixture`, `pytest.mark.parametrize` e `pytest.raises`.

## Estrutura do projeto

```text
desafioTU/
├── validador.py
├── README.md
├── test/
│   └── test_validador.py
└── .venv/
```

> A pasta `.venv` é o ambiente virtual do Python. Ela não é necessária para versionar o projeto; pode ser recriada seguindo os passos abaixo.

## Pré-requisitos

- Python 3 instalado
- `pip` disponível no Python

Para verificar:

```bash
python --version
pip --version
```

## 1. Criar o ambiente virtual

Na pasta raiz do projeto, execute:

```bash
python -m venv .venv
```

## 2. Ativar o ambiente virtual

### Windows — CMD

```bash
.venv\Scripts\activate
```

### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal normalmente exibirá `(.venv)` no início da linha.

## 3. Instalar o pytest

```bash
python -m pip install pytest
```

Para verificar a instalação:

```bash
pytest --version
```

## 4. Executar todos os testes

Na pasta raiz do projeto, execute:

```bash
pytest
```

Também é possível utilizar:

```bash
python -m pytest
```

O pytest encontrará automaticamente os testes dentro da pasta `test`.

## 5. Executar somente o arquivo de testes

```bash
pytest test/test_validador.py
```

## 6. Executar um teste específico

Por exemplo, para executar somente os testes de validação de CEP:

```bash
pytest test/test_validador.py -k cep
```

Para executar somente os testes de CPF:

```bash
pytest test/test_validador.py -k cpf
```

Para executar somente os testes de CNPJ:

```bash
pytest test/test_validador.py -k cnpj
```

## 7. Entendendo o resultado

Quando todos os testes passam, o pytest apresenta uma saída semelhante a:

```text
============================= test session starts =============================
...
collected XX items

test/test_validador.py ....................                                [100%]

============================== XX passed in Xs ===============================
```

- `PASSED` / `passed`: teste executado com sucesso.
- `FAILED` / `failed`: o resultado obtido foi diferente do esperado.
- `ERROR`: ocorreu um erro durante a execução do teste.

## Recursos do pytest utilizados

### Fixture

A classe `Validador` é disponibilizada aos testes por meio de uma fixture:

```python
@pytest.fixture
def validador():
    return Validador()
```

### Parametrize

Os dados de teste são fornecidos utilizando:

```python
@pytest.mark.parametrize(...)
```

Isso permite executar o mesmo teste com diferentes valores.

### Raises

Os cenários em que um valor que não é `str` deve gerar `ValueError` são validados com:

```python
with pytest.raises(ValueError):
    validador.validar_cep(valor)
```

## Resumo dos cenários

Os testes contemplam:

- Valores válidos;
- Valores inválidos;
- Formatos com e sem máscara;
- Tamanhos inválidos;
- Numerações inválidas;
- Valores que não são do tipo `str`;
- Exceção `ValueError` para entradas que não são texto.

## Execução rápida

Depois de ativar o ambiente virtual e instalar o pytest, basta executar:

```bash
pytest
```
