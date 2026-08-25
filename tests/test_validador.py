import pytest
from validador import Validador


@pytest.fixture
def validador():
    return Validador()


@pytest.mark.parametrize(
    "cep",
    [
        "12345678",
        "50000000",
        "12345-678",
        "50000-000"
    ]
)
def test_validar_cep_valido(validador, cep):
    assert validador.validar_cep(cep) is True


@pytest.mark.parametrize(
    "cep",
    [
        "1234567",
        "123456789",
        "1234-5678",
        "12345-67",
        "123456-78",
        "abcdefgh",
        "12345-abc",
        "1234567a",
        "12345 678"
    ]
)
def test_validar_cep_invalido(validador, cep):
    assert validador.validar_cep(cep) is False


@pytest.mark.parametrize(
    "cep",
    [
        12345678,
        50000000,
        None,
        12345.678,
        True,
        ["12345678"]
    ]
)
def test_validar_cep_valor_nao_texto(validador, cep):
    with pytest.raises(ValueError):
        validador.validar_cep(cep)