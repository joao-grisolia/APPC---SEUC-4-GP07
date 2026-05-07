import os

def main():
    os.system('cls')
    printDelta9()
    somaPressoes = 0
    menorPressao = None
    contadorVerde = 0
    contadorLeituras = 0
    travou = False
    zonaAnterior = None
    
    numLeituras = int(input('Quantas leituras serão feitas: '))

    if numLeituras <= 0:
        print('Número de leituras deve ser maior que zero.')
        return

    for i in range(1, numLeituras+1):
        leitura = float(input(f'\nLeitura {i}: '))
        
        pressaoAjustada = ajustarPressao(leitura)
        somaPressoes += pressaoAjustada
        
        if menorPressao is None or pressaoAjustada < menorPressao:
            menorPressao = pressaoAjustada
        
        zonaAtual = classificarZona(pressaoAjustada)
        if zonaAtual == 'Verde': contadorVerde +=1
        contadorLeituras +=1
        
        print('-' * 20)
        print(f'Leitura: {pressaoAjustada:.2f} UPC')
        print(f'Zona:    {zonaAtual}')
        print('-' * 20)
        
        if zonaAnterior == 'Vermelha' and zonaAtual == 'Vermelha':
            travou = True
            break
        zonaAnterior = zonaAtual
    
    mediaDaPressoes = somaPressoes/contadorLeituras
    porcentagemVerdes  = (contadorVerde / contadorLeituras) * 100
    percentualRealizado = (contadorLeituras / numLeituras) * 100
    print('Todas as leituras foram realizadas, pressione ENTER para prosseguir')
    input()
    os.system('cls')
    printMetricas()
    print(f'Média das pressões: {mediaDaPressoes:.2f}')
    print(f'Menor pressão: {menorPressao:.2f}')
    print(f'% de leituras verdes: {porcentagemVerdes:.2f}%')
    
    if travou:
        print('Sistema travou por leituras vermelhas consecutivas')
        print(f'Percentual de leituras realizadas: {percentualRealizado:.2f}%')
    else:
        print('Sistema operou com sucesso')

def classificarZona(pressao):
    if 120 <= pressao <= 180:
        return 'Verde'
    elif pressao > 250:
        return 'Vermelha'
    else:
        return 'Amarela'

def ajustarPressao(leitura):
    if leitura > 150:
        return leitura * 1.08
    else:
        return leitura * 0.96
    

def printDelta9():
    print('''                                    
                                                       ,--.                                
,------.  ,------.,--.,--------. ,---.       ,---.     |  |    ,------.  ,------. ,------. 
|  .-.  \ |  .---'|  |'--.  .--'/  O  \     | o   \    |  |    |  .-.  \ |  .--. '|  .---' 
|  |  \  :|  `--, |  |   |  |  |  .-.  |    `..'  |    |  |    |  |  \  :|  '--' ||  `--,  
|  '--'  /|  `---.|  '--.|  |  |  | |  |     .'  /     |  |    |  '--'  /|  | --' |  `---. 
`-------' `------'`-----'`--'  `--' `--'     `--'      |  |    `-------' `--'     `------' 
                                                       `--'                                ''')
def printMetricas():
    print('''                                                                    
,--.   ,--.,------.,--------.,------. ,--. ,-----.  ,---.   ,---.   
|   `.'   ||  .---''--.  .--'|  .--. '|  |'  .--./ /  O  \ '   .-'  
|  |'.'|  ||  `--,    |  |   |  '--'.'|  ||  |    |  .-.  |`.  `-.  
|  |   |  ||  `---.   |  |   |  |\  \ |  |'  '--'\|  | |  |.-'    | 
`--'   `--'`------'   `--'   `--' '--'`--' `-----'`--' `--'`-----'  
                                                                    ''')

main()
