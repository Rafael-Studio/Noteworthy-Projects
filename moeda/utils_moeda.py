def aumentar(valor=0, taxa=0, formato=False):
    resultado = valor + (valor * taxa / 100)
    return resultado if not formato else moeda(resultado)


def diminuir(valor=0, taxa=0, formato=False):
    resultado = valor - (valor * taxa / 100)
    return resultado if not formato else moeda(resultado)


def dobro(valor=0, formato=False):
    resultado = valor * 2
    return resultado if not formato else moeda(resultado)


def metade(valor=0, formato=False):
    resultado = valor / 2
    return resultado if not formato else moeda(resultado)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)


def leiadinheiro(msg):
    check = False
    while not check:
        numero = input(msg).replace(',', '.').strip()
        if numero.isalpha() or numero == '':
            print(f'ERRO! "{numero}" não é um preço válido!')
        else:
            return float(numero)
