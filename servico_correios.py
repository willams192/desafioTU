import requests

class ServicoCorreios:
    
    def validar_cep_api(self, cep):
        if not isinstance(cep, str):
            raise ValueError("O CEP deve ser um texto")
        
        reposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if reposta.status_code == 200:
            return True 
        elif reposta.status_code == 400:
            return False
       