import pytest
from Validador import Validador

@pytest.fixture
def validador():
    return Validador()
    

@pytest.mark.parametrize("cpf",["52998224725","529.982.247-25","06025808031","060.258.080-31"])
def test_validar_cpf_valido(validador, cpf):    
    assert validador.validar_cpf(cpf) is True

@pytest.mark.parametrize("cpf",["11111111111","111.111.111-11","12345678900","123.456.789-00"])
def test_validar_cpf_invalido(validador, cpf):    
    assert validador.validar_cpf(cpf) is False

@pytest.mark.parametrize("cpf",[11111111111,12345678900,None,True,["52998224725"]])
def test_validar_cpf_nao_texto(validador, cpf):    
    with pytest.raises(ValueError):
        validador.validar_cpf(cpf)

@pytest.mark.parametrize("cnpj", ["11222333000181","11.222.333/0001-81","11144477000167","11.144.477/0001-67"])
def test_validar_cnpj_valido(validador, cnpj):
    assert validador.validar_cnpj(cnpj) is True


@pytest.mark.parametrize("cnpj", ["11111111111111","11.111.111/1111-11","12345678901234","12.345.678/9012-34"])
def test_validar_cnpj_invalido(validador, cnpj):
    assert validador.validar_cnpj(cnpj) is False


@pytest.mark.parametrize("cnpj", [11111111111111, 12345678901234, None, True, ["11222333000181"]])
def test_validar_cnpj_nao_texto(validador, cnpj):
    with pytest.raises(ValueError):
        validador.validar_cnpj(cnpj)