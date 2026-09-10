import pytest
from validador import Validador
from servico_correios import ServicoCorreios

@pytest.fixture
def validador():
    return Validador()

@pytest.fixture
def servico_correios():
    return ServicoCorreios()

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

@pytest.mark.parametrize("cep",["12345678","50000000","12345-678","50000-000"])
def test_validar_cep_valido(validador, cep):
    assert validador.validar_cep(cep) is True


@pytest.mark.parametrize("cep",["1234567","123456789","1234-5678","12345-67","123456-78","abcdefgh","12345-abc","1234567a","12345 678"])
def test_validar_cep_invalido(validador, cep):
    assert validador.validar_cep(cep) is False


@pytest.mark.parametrize("cep",[12345678,50000000,None,12345.678,True,["12345678"]])
def test_validar_cep_valor_nao_texto(validador, cep):
    with pytest.raises(ValueError):
        validador.validar_cep(cep)

@pytest.mark.parametrize("cep",["12345678","50000000","12345-678","50000-000"])
def test_validar_cep_valido_por_API(servico_correios, cep, mocker):
    mock_resposta = mocker.Mock()
    mock_resposta.status_code = 200
    mock_resposta.json.return_value = {"cep": cep, "logradouro": "Rua Exemplo"}
    
    mock_patcher = mocker.patch("servico_correios.requests.get", return_value=mock_resposta)

    assert servico_correios.validar_cep_api(cep) is True
    mock_patcher.assert_called_once_with(f"https://viacep.com.br/ws/{cep}/json/") 


@pytest.mark.parametrize("cep",["1234567","123456789","1234-5678","12345-67","123456-78","abcdefgh","12345-abc","1234567a","12345 678"])
def test_validar_cep_invalido_por_API(servico_correios, cep, mocker):
    mock_resposta = mocker.Mock()
    mock_resposta.status_code = 400
    mock_resposta.json.return_value = {"erro": "CEP não encontrado"}

    mock_patcher = mocker.patch("servico_correios.requests.get", return_value=mock_resposta)
    # 2. Executa a validação sem bater na API real
    assert servico_correios.validar_cep_api(cep) is False
    mock_patcher.assert_called_once_with(f"https://viacep.com.br/ws/{cep}/json/") 


@pytest.mark.parametrize("cep",[12345678,50000000,None,12345.678,True,["12345678"]])
def test_validar_cep_valor_nao_texto_por_API(servico_correios, cep):
    with pytest.raises(ValueError):
        servico_correios.validar_cep_api(cep)