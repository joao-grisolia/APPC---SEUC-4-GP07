# ==================================================================
#  SEUC-4 - Sistema de Escoamento de Unidades de Carga
#  Refinaria Delta-9 - Sentinela de Fluxo (sem memoria de armazenamento)
# ==================================================================

import os


def preparar_terminal():
    os.system("")
    os.system("cls")


def limpar_tela():
    os.system("cls")


def banner():
    print( "  ____  _____ _   _  ____      _  _   " )
    print( " / ___|| ____| | | |/ ___|    | || |  " )
    print( " \\___ \\|  _| | | | | |   _____| || |_ " )
    print( "  ___) | |___| |_| | |__|_____|__   _|" )
    print( " |____/|_____|\\___/ \\____|       |_|  " )
    print("  Sistema de Escoamento de Unidades de Carga - v4.0" )
    print("  Refinaria Delta-9  |  Duto Principal de Escoamento" )
    print("  ----------------------------------------------------" )


def ler_nome_operador():
    nome = input("Digite o nome do operador: ")

def ler_inteiro_positivo(mensagem):
    valor = int(input(mensagem))
    while valor <= 0:
        print("  [ERRO] Valor invalido. Digite um inteiro maior que zero." )
        valor = int(input(mensagem))
    return valor


def ler_pressao_valida(indice):
    print("  ------------------------------------------------------" )
    print("  >> LEITURA Nº", indice)
    pressao = float(input("  Pressao hidrodinamica medida (UPC): "))
    while pressao <= 0:
        print("  [ERRO] Pressao deve ser maior que zero." )
        pressao = float(input("  Pressao hidrodinamica medida (UPC): "))
    return pressao


def ajustar_pressao(pressao):
    if pressao > 150:
        ajustada = pressao * 1.08
        rotulo = "EXPANSAO TERMICA (+8%)"
    else:
        ajustada = pressao * 0.96
        rotulo = "CONTRACAO TERMICA (-4%)"
    print( "  > Ajuste:", rotulo)
    return ajustada


def classificar_zona(pressao_ajustada):
    if pressao_ajustada >= 120 and pressao_ajustada <= 180:
        return 1
    if pressao_ajustada > 250:
        return 3
    return 2


def exibir_zona(codigo_zona, pressao_ajustada):
    print("  > Pressao ajustada:", round(pressao_ajustada, 2), "UPC" )
    if codigo_zona == 1:
        print("  [ ZONA VERDE ]   Estavel - escoamento nominal." )
    elif codigo_zona == 2:
        print("  [ ZONA AMARELA ] Oscilacao detectada - atencao." )
    else:
        print("  [ ZONA VERMELHA ] CRITICA - risco de fadiga!" )


def exibir_tendencia(ajustada, anterior, qtd_realizadas):
    if qtd_realizadas == 1:
        print("  > Tendencia: -- (referencia inicial)")
        return
    if ajustada > anterior:
        print("  > Tendencia: SUBINDO  (delta +"
              + str(round(ajustada - anterior, 2)) + " UPC)")
    elif ajustada < anterior:
        print("  > Tendencia: DESCENDO (delta -"
              + str(round(anterior - ajustada, 2)) + " UPC)")
    else:
        print("  > Tendencia: ESTAVEL  (sem variacao)")


def alerta_travamento():
    print("  ####################################################" )
    print("  #   !!! PROTOCOLO DE TRAVAMENTO ACIONADO !!!       #" )
    print("  #   Duas leituras consecutivas em ZONA VERMELHA.   #" )
    print("  #   Escoamento INTERROMPIDO por seguranca.         #" )
    print("  ####################################################" )


def indice_integridade(qtd_verde, qtd_amarela, qtd_vermelha, qtd_realizadas):
    if qtd_realizadas == 0:
        return 0.0
    pontos = (qtd_verde * 1.0) + (qtd_amarela * 0.5) + (qtd_vermelha * 0.0)
    return (pontos / qtd_realizadas) * 100


def classificar_integridade(indice):
    if indice >= 80:
        return "EXCELENTE" 
    if indice >= 60:
        return "BOM" 
    if indice >= 40:
        return "REGULAR" 
    if indice >= 20:
        return "PRECARIO" 
    return "CRITICO" 


def exibir_metricas(soma_ajustadas, qtd_realizadas, qtd_total,
                    menor_pressao, maior_pressao,
                    qtd_verde, qtd_amarela, qtd_vermelha, travou):
    print()
    print("==================================================================" )
    print("          RELATORIO FINAL DE TURNO  -  SEUC-4 / Delta-9" )
    print("==================================================================" )

    if qtd_realizadas == 0:
        print("Nenhuma leitura foi realizada. Relatorio vazio." )
        return

    media = soma_ajustadas / qtd_realizadas
    perc_verde = (qtd_verde / qtd_realizadas) * 100
    perc_amarela = (qtd_amarela / qtd_realizadas) * 100
    perc_vermelha = (qtd_vermelha / qtd_realizadas) * 100
    integridade = indice_integridade(qtd_verde, qtd_amarela,
                                     qtd_vermelha, qtd_realizadas)

    print("  Leituras realizadas .........:", qtd_realizadas, "/", qtd_total)
    print("  Media das pressoes ajustadas :", round(media, 2), "UPC")
    print("  Menor pressao registrada ....:",
          round(menor_pressao, 2), "UPC" )
    print("  Maior pressao registrada ....:",
          round(maior_pressao, 2), "UPC" )
    print()
    print("  Distribuicao de zonas:" )
    print("    Zona Verde   :", qtd_verde, "leituras  (",
          round(perc_verde, 2), "% )" )
    print("    Zona Amarela :", qtd_amarela, "leituras  (",
          round(perc_amarela, 2), "% )" )
    print("    Zona Vermelha:", qtd_vermelha, "leituras  (",
          round(perc_vermelha, 2), "% )" )
    print()
    print("  Indice de Integridade do Duto:",
          round(integridade, 2), "/ 100  ->",
          classificar_integridade(integridade))

    if travou:
        perc_realizado = (qtd_realizadas / qtd_total) * 100
        print()
        print("  STATUS FINAL: TRAVADO POR SEGURANCA" )
        print("  Percentual do turno executado:",
              round(perc_realizado, 2), "%" )
    else:
        print()
        print("  STATUS FINAL: TURNO CONCLUIDO COM SUCESSO" )

    print("==================================================================" )


def main():
    preparar_terminal()
    banner()

    operador = ler_nome_operador()
    total = ler_inteiro_positivo("  Informe o numero total de leituras do turno: ")

    soma_ajustadas = 0.0
    menor_pressao = 0.0
    maior_pressao = 0.0
    qtd_verde = 0
    qtd_amarela = 0
    qtd_vermelha = 0
    qtd_realizadas = 0
    zona_anterior = 0
    pressao_anterior = 0.0
    travou = False
    i = 1

    while i <= total and travou == False:
        pressao = ler_pressao_valida(i)
        ajustada = ajustar_pressao(pressao)
        zona = classificar_zona(ajustada)
        exibir_zona(zona, ajustada)
        exibir_tendencia (ajustada, pressao_anterior, qtd_realizadas + 1)

        soma_ajustadas = soma_ajustadas + ajustada
        qtd_realizadas = qtd_realizadas + 1

        if qtd_realizadas == 1:
            menor_pressao = ajustada
            maior_pressao = ajustada
        else:
            if ajustada < menor_pressao:
                menor_pressao = ajustada
            if ajustada > maior_pressao:
                maior_pressao = ajustada

        if zona == 1:
            qtd_verde = qtd_verde + 1
        elif zona == 2:
            qtd_amarela = qtd_amarela + 1
        else:
            qtd_vermelha = qtd_vermelha + 1

        if zona == 3 and zona_anterior == 3:
            alerta_travamento()
            travou = True


        zona_anterior = zona
        pressao_anterior = ajustada
        i = i + 1

    exibir_metricas(soma_ajustadas, qtd_realizadas, total,
                    menor_pressao, maior_pressao,
                    qtd_verde, qtd_amarela, qtd_vermelha, travou)


main()