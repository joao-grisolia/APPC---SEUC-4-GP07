import os
import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_int(prompt, attempts=3):
    if attempts <= 0:
        raise ValueError("Máximo de tentativas excedido. Reinicie o programa.")
    try:
        val = input(prompt).strip()
        num = int(val)
        if num <= 0:
            raise ValueError("Deve ser um número inteiro positivo.")
        return num
    except ValueError:
        print("Entrada inválida. Deve ser um número inteiro positivo. Tentativas restantes:", attempts - 1)
        return get_int(prompt, attempts - 1)

def get_float(prompt, attempts=3):
    if attempts <= 0:
        raise ValueError("Máximo de tentativas excedido. Reinicie o programa.")
    try:
        val = input(prompt).replace(',', '.').strip()
        num = float(val)
        if num <= 0:
            raise ValueError("Deve ser um número positivo.")
        return num
    except ValueError:
        print("Entrada inválida. Deve ser um número positivo (use . para decimal). Tentativas restantes:", attempts - 1)
        return get_float(prompt, attempts - 1)

def adjust_thermal(pressure):
    if pressure > 150:
        return pressure * 1.08
    else:
        return pressure * 0.96

def classify_zone(pressure):
    if 120 <= pressure <= 180:
        return "Verde"
    elif pressure < 250:
        return "Amarela"
    else:
        return "Vermelha"

# Programa principal
clear_screen()
print("=== SISTEMA DE ESCOAMENTO DE UNIDADES DE CARGA (SEUC-4) ===")
start_dt = datetime.datetime.now()
print(f"Iniciado em: {start_dt.strftime('%d/%m/%Y %H:%M:%S')}")

operador = input("Nome do operador: ").strip() or "Não informado"

n_total = get_int("Número total de leituras de pressão: ")

pressures_raw = []
pressures_adj = []
zones = []
consecutive_red = 0
interrupted = False
actual_readings = 0

print("\nIniciando leituras... (Pressione Enter após cada leitura)")

for i in range(n_total):
    try:
        raw_pressure = get_float(f"Leitura {i+1}/{n_total} - Pressão atual (UPCs): ")
        pressures_raw.append(raw_pressure)
        
        adj_pressure = adjust_thermal(raw_pressure)
        pressures_adj.append(adj_pressure)
        
        zone = classify_zone(adj_pressure)
        zones.append(zone)
        
        actual_readings += 1
        
        if zone == "Vermelha":
            consecutive_red += 1
        else:
            consecutive_red = 0
        
        if consecutive_red >= 2:
            interrupted = True
            print("\n*** ALERTA: TRAVAMENTO DETECTADO! 2 leituras consecutivas na Zona Vermelha. ***")
            print("Sistema interrompido.")
            break
        
        print(f"  -> Ajustada: {adj_pressure:.2f} UPCs | Zona: {zone}")
        
    except ValueError as e:
        print(f"Erro na leitura {i+1}: {e}")
        print("Pulando esta leitura.")
        continue

end_dt = datetime.datetime.now()
print("\n" + "="*50)
print("=== MÉTRICAS FINAIS ===")
print(f"Operador: {operador}")
print(f"Leituras totais planejadas: {n_total}")

if pressures_adj:
    avg_pressure = sum(pressures_adj) / len(pressures_adj)
    min_pressure = min(pressures_adj)
    max_pressure = max(pressures_adj)
    green_count = zones.count("Verde")
    green_pct = (green_count / len(zones)) * 100
    
    print(f"Média das pressões ajustadas: {avg_pressure:.2f} UPCs")
    print(f"Menor pressão registrada: {min_pressure:.2f} UPCs")
    print(f"Maior pressão registrada: {max_pressure:.2f} UPCs")
    print(f"Percentual na Zona Verde: {green_pct:.1f}% ({green_count}/{len(zones)})")
    
    performed_pct = (actual_readings / n_total) * 100
    status = "(completo)" if not interrupted else "(interrompido por travamento)"
    print(f"Percentual de leituras realizadas: {performed_pct:.1f}% {status}")
else:
    print("Nenhuma leitura válida realizada.")

print(f"Finalizado em: {end_dt.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Tempo decorrido: {end_dt - start_dt}")
print("="*50)
