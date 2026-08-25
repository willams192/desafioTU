class Validador:

    def validar_cep(self, cep):
        if not isinstance(cep, str):
            raise ValueError("O CEP deve ser um texto")

        if len(cep) == 8:
            return cep.isdigit()

        if len(cep) == 9:
            return (
                cep[:5].isdigit()
                and cep[5] == "-"
                and cep[6:].isdigit()
            )

        return False