from validate_docbr import CPF

class Cpf:
    _cpfValidator = CPF()

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            return self._cpfValidator.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def format_cpf(self):
        return self._cpfValidator.mask(self.cpf)