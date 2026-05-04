# ==================================================================
#  SEUC-4 - Sistema de Escoamento de Unidades de Carga
#  Refinaria Delta-9 - Sentinela de Fluxo (sem memoria de armazenamento)
# ==================================================================

import os


# ---------- Cores ANSI (ativadas via os.system) -------------------
RESET = "\033[0m"
NEG = "\033[1m"
VRD = "\033[92m"
AMR = "\033[93m"
VML = "\033[91m"
CIA = "\033[96m"
MAG = "\033[95m"
CIN = "\033[90m"


def preparar_terminal():
    os.system("")
    os.system("cls")


def limpar_tela():
    os.system("cls")


def banner():
    print(CIA + "  ____  _____ _   _  ____      _  _   " + RESET)
    print(CIA + " / ___|| ____| | | |/ ___|    | || |  " + RESET)
    print(CIA + " \\___ \\|  _| | | | | |   _____| || |_ " + RESET)
    print(CIA + "  ___) | |___| |_| | |__|_____|__   _|" + RESET)
    print(CIA + " |____/|_____|\\___/ \\____|       |_|  " + RESET)
    print(MAG + "  Sistema de Escoamento de Unidades de Carga - v4.0" + RESET)
    print(CIN + "  Refinaria Delta-9  |  Duto Principal de Escoamento" + RESET)
    print(CIN + "  ----------------------------------------------------" + RESET)


def ler_nome_operador():
    nome = input("Digite o nome do operador: ")

def ler_inteiro_positivo(mensagem):
    valor = int(input(mensagem))
    while valor <= 0:
        print(VML + "  [ERRO] Valor invalido. Digite um inteiro maior que zero." + RESET)
        valor = int(input(mensagem))
    return valor


def ler_pressao_valida(indice):
    print(CIN + "  ------------------------------------------------------" + RESET)
    print(NEG + "  >> LEITURA Nº", indice, RESET)
    pressao = float(input("  Pressao hidrodinamica medida (UPC): "))
    while pressao <= 0:
        print(VML + "  [ERRO] Pressao deve ser maior que zero." + RESET)
        pressao = float(input("  Pressao hidrodinamica medida (UPC): "))
    return pressao


def ajustar_pressao(pressao):
    if pressao > 150:
        ajustada = pressao * 1.08
        rotulo = "EXPANSAO TERMICA (+8%)"
    else:
        ajustada = pressao * 0.96
        rotulo = "CONTRACAO TERMICA (-4%)"
    print(CIA + "  > Ajuste:", rotulo, RESET)
    return ajustada


def classificar_zona(pressao_ajustada):
    if pressao_ajustada >= 120 and pressao_ajustada <= 180:
        return 1
    if pressao_ajustada > 250:
        return 3
    return 2


def exibir_zona(codigo_zona, pressao_ajustada):
    print(CIN + "  > Pressao ajustada:", round(pressao_ajustada, 2), "UPC" + RESET)
    if codigo_zona == 1:
        print(VRD + NEG + "  [ ZONA VERDE ]   Estavel - escoamento nominal." + RESET)
    elif codigo_zona == 2:
        print(AMR + NEG + "  [ ZONA AMARELA ] Oscilacao detectada - atencao." + RESET)
    else:
        print(VML + NEG + "  [ ZONA VERMELHA ] CRITICA - risco de fadiga!" + RESET)


def exibir_tendencia(ajustada, anterior, qtd_realizadas):
    if qtd_realizadas == 1:
        print(CIN + "  > Tendencia: -- (referencia inicial)" + RESET)
        return
    if ajustada > anterior:
        print(VML + "  > Tendencia: SUBINDO  (delta +"
              + str(round(ajustada - anterior, 2)) + " UPC)" + RESET)
    elif ajustada < anterior:
        print(VRD + "  > Tendencia: DESCENDO (delta -"
              + str(round(anterior - ajustada, 2)) + " UPC)" + RESET)
    else:
        print(AMR + "  > Tendencia: ESTAVEL  (sem variacao)" + RESET)


def barra_progresso(realizadas, total):
    largura = 30
    preenchido = int((realizadas / total) * largura)
    barra = ""
    i = 0
    while i < largura:
        if i < preenchido:
            barra = barra + "#"
        else:
            barra = barra + "-"
        i = i + 1
    percent = round((realizadas / total) * 100, 1)
    print(MAG + "  Progresso do turno: [" + barra + "] "
          + str(percent) + "%" + RESET)


def alerta_travamento():
    print(VML + NEG + "  ####################################################" + RESET)
    print(VML + NEG + "  #   !!! PROTOCOLO DE TRAVAMENTO ACIONADO !!!       #" + RESET)
    print(VML + NEG + "  #   Duas leituras consecutivas em ZONA VERMELHA.   #" + RESET)
    print(VML + NEG + "  #   Escoamento INTERROMPIDO por seguranca.         #" + RESET)
    print(VML + NEG + "  ####################################################" + RESET)


def indice_integridade(qtd_verde, qtd_amarela, qtd_vermelha, qtd_realizadas):
    if qtd_realizadas == 0:
        return 0.0
    pontos = (qtd_verde * 1.0) + (qtd_amarela * 0.5) + (qtd_vermelha * 0.0)
    return (pontos / qtd_realizadas) * 100


def classificar_integridade(indice):
    if indice >= 80:
        return VRD + "EXCELENTE" + RESET
    if indice >= 60:
        return VRD + "BOM" + RESET
    if indice >= 40:
        return AMR + "REGULAR" + RESET
    if indice >= 20:
        return AMR + "PRECARIO" + RESET
    return VML + "CRITICO" + RESET


def exibir_metricas(soma_ajustadas, qtd_realizadas, qtd_total,
                    menor_pressao, maior_pressao,
                    qtd_verde, qtd_amarela, qtd_vermelha, travou):
    print()
    print(CIA + NEG + "==================================================================" + RESET)
    print(CIA + NEG + "          RELATORIO FINAL DE TURNO  -  SEUC-4 / Delta-9" + RESET)
    print(CIA + NEG + "==================================================================" + RESET)

    if qtd_realizadas == 0:
        print(VML + "Nenhuma leitura foi realizada. Relatorio vazio." + RESET)
        return

    media = soma_ajustadas / qtd_realizadas
    perc_verde = (qtd_verde / qtd_realizadas) * 100
    perc_amarela = (qtd_amarela / qtd_realizadas) * 100
    perc_vermelha = (qtd_vermelha / qtd_realizadas) * 100
    integridade = indice_integridade(qtd_verde, qtd_amarela,
                                     qtd_vermelha, qtd_realizadas)

    print("  Leituras realizadas .........:", qtd_realizadas, "/", qtd_total)
    print("  Media das pressoes ajustadas :", round(media, 2), "UPC")
    print(VRD + "  Menor pressao registrada ....:",
          round(menor_pressao, 2), "UPC" + RESET)
    print(VML + "  Maior pressao registrada ....:",
          round(maior_pressao, 2), "UPC" + RESET)
    print()
    print(CIN + "  Distribuicao de zonas:" + RESET)
    print(VRD + "    Zona Verde   :", qtd_verde, "leituras  (",
          round(perc_verde, 2), "% )" + RESET)
    print(AMR + "    Zona Amarela :", qtd_amarela, "leituras  (",
          round(perc_amarela, 2), "% )" + RESET)
    print(VML + "    Zona Vermelha:", qtd_vermelha, "leituras  (",
          round(perc_vermelha, 2), "% )" + RESET)
    print()
    print(MAG + "  Indice de Integridade do Duto:",
          round(integridade, 2), "/ 100  ->",
          classificar_integridade(integridade))

    if travou:
        perc_realizado = (qtd_realizadas / qtd_total) * 100
        print()
        print(VML + NEG + "  STATUS FINAL: TRAVADO POR SEGURANCA" + RESET)
        print(VML + "  Percentual do turno executado:",
              round(perc_realizado, 2), "%" + RESET)
    else:
        print()
        print(VRD + NEG + "  STATUS FINAL: TURNO CONCLUIDO COM SUCESSO" + RESET)

    print(CIA + NEG + "==================================================================" + RESET)


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
        exibir_tendencia(ajustada, pressao_anterior, qtd_realizadas + 1)

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

        barra_progresso(qtd_realizadas, total)

        zona_anterior = zona
        pressao_anterior = ajustada
        i = i + 1

    exibir_metricas(soma_ajustadas, qtd_realizadas, total,
                    menor_pressao, maior_pressao,
                    qtd_verde, qtd_amarela, qtd_vermelha, travou)


main()