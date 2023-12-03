from acesso_cep import BuscaEndereco
from cpf_cnpj import Documento
from datas import DatasBr
from telefone import TelefonesBr

exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

telefone = "2126481234"
telefone_objeto = TelefonesBr(telefone)

cadastro = DatasBr()
print(cadastro.format_data())

hoje = DatasBr()
print(hoje.tempo_cadastro())

cep = "03475170"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.retorna_endereco()

print(bairro, cidade, uf)