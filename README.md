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
ou 
```bash
python -m pytest
```
