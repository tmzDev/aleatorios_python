import requests

cep = input("Informe o cep : ")
requisicao = requests.get(f"https://cep.awesomeapi.com.br//{cep}")
#print(requisicao.json())
req_dct = requisicao.json()


print(f'''Cep : {cep} \nEndereço : {req_dct["address_type"]} {req_dct["address_name"]} \nBairro : {req_dct["district"]}
Cidade : {req_dct["city"]} \nDDD : 0{req_dct["ddd"]}''')
