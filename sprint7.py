import requests
import os
import xmltodict
from pathlib import Path

def main():
    os.system('cls') or None

    print('####################')
    print('### Busca Cep ###')
    print('####################')
    print('')

    input_cep = input('Digite o Cep para a consulta: ')

    if len(input_cep) != 8:
        print('QUANTIDADE DE DIGITOS NÃO É VÁLIDA')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json'.format(input_cep))
    address = request.json()

    if 'erro' not in address:
        print('------CEP ENCONTRADO------')
        print('CEP: {}'.format(address['cep']))
        print('LOGRADOURO: {}'.format(address['logradouro']))
        print('COMPLEMENTO: {}'.format(address['complemento']))
        print('BAIRRO: {}'.format(address['bairro']))
        print('CIDADE: {}'.format(address['localidade']))
        print('ESTADO: {}'.format(address['uf']))

    else:
        print('{}: CEP INVÁLIDO.'.format(input_cep))

    print('----------------------------')
    option = int(input('Deseja Salvar a consulta ?\n1. SIM\n2. SAIR\n'))
    if option == 1:
        print(address)

    
if __name__ == '__main__':
    main()

