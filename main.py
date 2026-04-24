import os

lista = []
lista_zonas = []
def main():
    os.system('cls')
    nome = str(input('Digite seu nome: ')).strip()
    numLeituras = int(input('Digite o número de leituras: '))
    
    for i in range(numLeituras):
        leitura = float(input(f'Leitura {i + 1}: '))
        leitura = ajusteTermico(leitura)
        zona = verificarZona(leitura)
        lista.append(leitura)
        print(f'Leitura {i + 1} de {numLeituras} registrada: {leitura:.2f}')
        print(f'Zona: {zona}')
        print('-' * 30)
        print(f'Leituras registradas até agora: {lista}')
        print('-' * 30)
    print(lista)
        

def ajusteTermico(leitura):
    if leitura > 150:
        leitura *= 1.08
    else:
        leitura *= 0.96
    return leitura

def verificarZona(leitura):
    
    if 120 <= leitura <= 180:
        return 'Verde'
    elif leitura < 250:
        return 'Amarela'
    else:
        lista_zonas.append('Vermelha')
        if lista_zonas.count('Vermelha') >= 2:
            print('Sistema interrompido devido a 2 leituras consecutivas na Zona Vermelha.')
            metricasFinais()
        return 'Vermelha'
        

def metricasFinais():
    return False

main()