import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])

    def retorna_endereco(cep):
        url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        r = requests.get(url)
        dados = r.json()
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        return bairro, cidade, uf