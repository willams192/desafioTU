class Validador:

    def validar_cpf(self, valor) -> bool:
        if not isinstance(valor, str):
            raise ValueError("O CPF deve ser fornecido como texto (string).")

        cpf = ''.join(filter(str.isdigit, valor))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        digito1 = self.calcular_digito(cpf[:9])
        digito2 = self.calcular_digito(cpf[:9] + digito1)

        return cpf[-2:] == digito1 + digito2

    def validar_cnpj(self, valor) -> bool:
        if not isinstance(valor, str):
            raise ValueError("O CNPJ deve ser fornecido como texto (string).")

        cnpj = ''.join(filter(str.isdigit, valor))

        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False
        
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        digito1 = self.calcular_digito(cnpj[:12], pesos1)
        digito2 = self.calcular_digito(cnpj[:12] + digito1, pesos2)
        return cnpj[-2:] == digito1 + digito2

    def calcular_digito(self, base, pesos=None) -> str:
            if pesos is None:
                pesos = range(len(base) + 1, 1, -1)
            soma = sum(int(d) * p for d, p in zip(base, pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)
