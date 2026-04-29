import os

def main():
    os.system('cls')
    printDelta9()
    somaPressoes = 0
    menorPressao = 0
    contadorVerde = 0
    contadorLeituras = 0
    travou = False
    zonaAnterior = None
    
    numLeituras = int(input('Quantas leituras serão feitas: '))
    for i in range(1, numLeituras+1):
        leitura = float(input(f'\nLeitura {i}: '))
        
        pressaoAjustada = ajustarPressao(leitura)
        somaPressoes += pressaoAjustada
        
        if pressaoAjustada < menorPressao: menorPressao = pressaoAjustada
        
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
    print('Todas a leituras foram realizadas, pressione ENTER para prosseguir')
    input()
    os.system('cls')
    printMetricas()
    print(f'Média das pressões: {mediaDaPressoes:.2f}')
    print(f'Menor pressão: {menorPressao:.2f}')
    print(f'% de leituras verdes: {porcentagemVerdes:.2f}%')
    
    if travou:
        print('sistema travou por leituras vermelhas consecutivas')
    else:
        print('Sistema operou normalmente')

def classificarZona(pressao):
    if 120 <= pressao <= 180:
        return 'Verde'
    elif pressao < 250:
        return 'Amarela'
    else:
        return 'Vermelha'

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


