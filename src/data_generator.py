# Arquivo: src/data_generator.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# --- Configurações da Simulação ---
NUM_REGISTROS = 2000
TAXA_EVASAO = 0.15  # 15% de pacientes desistem
DATA_BASE = datetime(2025, 10, 30)

def gerar_logs_atendimento(df_medicos):
    """
    Gera logs de atendimento simulados, refletindo alta variabilidade e tempo de espera (4h médio).
    """
    print("Iniciando geração de 2.000 logs de atendimento...")
    
    # Lista de IDs de médicos (para sorteio)
    medicos_ids = df_medicos['id_medico'].unique()
    
    # Lista de IDs de médicos (para sorteio)
    medicos_ids = df_medicos['id_medico'].unique()
    
    # Probabilidade de ser atendido: 1.0 - TAXA_EVASAO (1 - 0.15 = 0.85)
    # Probabilidade de desistir: TAXA_EVASAO (0.15)
    PROB_ATENDIDO = 1.0 - TAXA_EVASAO
    
    dados = {
        'id_atendimento': np.arange(1000, 1000 + NUM_REGISTROS),
        'data_chegada': [DATA_BASE.strftime('%Y-%m-%d')] * NUM_REGISTROS,
        'hora_checkin': [],
        'id_medico': np.random.choice(medicos_ids, NUM_REGISTROS),
        # CORREÇÃO APLICADA: Simplifica o sorteio para apenas Atendido (85%) e Desistiu (15%)
        'status': np.random.choice(['Atendido', 'Desistiu'], 
                                   NUM_REGISTROS, 
                                   p=[PROB_ATENDIDO, TAXA_EVASAO])
    }
    # 1. Simulação do Check-in
    # Check-ins distribuídos entre 8h e 16h
    checkin_segundos = np.random.randint(8 * 3600, 16 * 3600, NUM_REGISTROS)
    dados['hora_checkin'] = [timedelta(seconds=int(s)) for s in checkin_segundos]

    df_logs = pd.DataFrame(dados)
    
    # 2. Simulação do Tempo de Espera (O Problema do Negócio)
    
    # Gerar o tempo de espera (em segundos)
    # A média deve ser próxima de 4h (14.400 segundos), mas com alta variabilidade (picos de 8h/28.800s)
    
    # Usaremos uma distribuição skewed (distorcida) para simular a fila acumulando
    # Média de 14400 segundos (4h), mas com cauda longa (picos)
    tempo_espera_segundos = np.abs(np.random.normal(loc=14400, scale=8000, size=NUM_REGISTROS)).clip(min=600, max=30000) # Mínimo de 10 min, Máximo de ~8.3h
    
    # 3. Calcular Hora de Início e Fim da Consulta
    df_logs['hora_consulta_inicio'] = df_logs.apply(
        lambda row: row['hora_checkin'] + timedelta(seconds=int(tempo_espera_segundos[row.name])),
        axis=1
    )
    
    # Simular o Tempo de Ciclo (Consulta) baseado no Perfil de Variabilidade do Médico
    df_logs = df_logs.merge(df_medicos[['id_medico', 'perfil_variabilidade']], on='id_medico', how='left')
    
    def gerar_tempo_consulta(row):
        perfil = row['perfil_variabilidade']
        if perfil == 'Baixa':
            # Baixa variabilidade: 10 a 15 min (600 a 900s)
            return np.random.randint(600, 900)
        elif perfil == 'Média':
            # Média: 15 a 30 min (900 a 1800s)
            return np.random.randint(900, 1800)
        elif perfil == 'Alta':
            # Alta: 30 a 50 min (1800 a 3000s)
            return np.random.randint(1800, 3000)
        elif perfil == 'Altíssima':
             # Altíssima: 30 a 55 min (1800 a 3300s) - O pico do problema!
            return np.random.randint(1800, 3300)
        return 1200 # Padrão
    
    df_logs['tempo_consulta_seg'] = df_logs.apply(gerar_tempo_consulta, axis=1)
    
    df_logs['hora_consulta_fim'] = df_logs.apply(
        lambda row: row['hora_consulta_inicio'] + timedelta(seconds=int(row['tempo_consulta_seg'])),
        axis=1
    )
    
    # 4. Tratamento da Evasão (Status 'Desistiu')
    # Pacientes que desistiram não têm hora_consulta_inicio ou hora_consulta_fim
    df_logs.loc[df_logs['status'] == 'Desistiu', ['hora_consulta_inicio', 'hora_consulta_fim']] = np.nan
    
    # Formatação de Saída
    df_logs['hora_checkin'] = df_logs['hora_checkin'].astype(str).str.split().str[-1]
    df_logs['hora_consulta_inicio'] = df_logs['hora_consulta_inicio'].astype(str).str.split().str[-1].replace('NaT', '')
    df_logs['hora_consulta_fim'] = df_logs['hora_consulta_fim'].astype(str).str.split().str[-1].replace('NaT', '')
    
    # Selecionar e ordenar colunas finais
    df_logs = df_logs[['id_atendimento', 'data_chegada', 'hora_checkin', 'hora_consulta_inicio', 
                       'hora_consulta_fim', 'id_medico', 'status']]
    
    return df_logs


def main():
    """Função principal para gerar e salvar os dados."""
    
    caminho_base = os.path.dirname(os.path.abspath(__file__)).replace('src', '')
    caminho_raw = os.path.join(caminho_base, 'data', 'raw')
    
       
    # 1. Ler a dimensão de médicos
    caminho_medicos = os.path.join(caminho_raw, 'escala_medicos.csv')
    
    # --- INÍCIO DO TRATAMENTO DE LEITURA ROBUSTA COM MÚLTIPLAS ENCODINGS ---
    df_medicos = None # Inicializa para garantir que a variável exista
    encoding_tentativas = ['utf-8-sig', 'latin-1', 'iso-8859-1', 'utf-8']
    
    for encoding in encoding_tentativas:
        try:
            # Força o separador ponto-e-vírgula (;), tenta a codificação e desativa a leitura de aspas
            df_medicos = pd.read_csv(caminho_medicos, 
                                     sep=';', 
                                     encoding=encoding, 
                                     quoting=3, # Desativa a leitura de aspas
                                     engine='python')  # Engine mais robusto para parsing
                                      # Engine mais robusto para parsing
            print(f"SUCESSO: Arquivo de médicos lido com encoding: {encoding}")
            break
        except FileNotFoundError:
            print(f"ERRO: Arquivo {caminho_medicos} não encontrado.")
            return
        except (UnicodeDecodeError, pd.errors.EmptyDataError):
            continue
        except Exception as e:
            print(f"ERRO CRÍTICO na leitura do CSV: {e}")
            return
    
    if df_medicos is None:
        print("\n" + "="*70)
        print("FALHA CRÍTICA: Não foi possível ler o arquivo 'escala_medicos.csv' com nenhuma codificação.")
        print("Verifique se o arquivo está na pasta data/raw/ e se não está corrompido.")
        print("="*70)
        return

    # A LIMPEZA ROBUSTA: (Remove apenas espaços, mantendo underscores)
    df_medicos.columns = df_medicos.columns.str.strip()
    # --- NOVO AJUSTE: REMOVER AS ASPAS QUE SOBRARAM ---
    df_medicos.columns = df_medicos.columns.str.replace('"', '')
    
    # Validação Pós-Limpeza (Checa as duas formas possíveis do nome da coluna)
    if 'id_medico' not in df_medicos.columns or ('perfil_variabilidade' not in df_medicos.columns and 'perfilvariabilidade' not in df_medicos.columns):
        print("\n" + "="*70)
        print("ERRO CRÍTICO: As colunas chave não foram encontradas após a limpeza de espaços.")
        print(f"Colunas encontradas: {list(df_medicos.columns)}")
        print("Verifique o cabeçalho do CSV: id_medico;nome_medico;especialidade;perfil_variabilidade.")
        print("="*70)
        return
    # --- FIM DO TRATAMENTO DE LEITURA ROBUSTA ---
    
           
    # 2. Gerar logs
    df_logs = gerar_logs_atendimento(df_medicos)
    
    # 3. Salvar o arquivo FATO
    caminho_logs_output = os.path.join(caminho_raw, 'logs_atendimento.csv')
    df_logs.to_csv(caminho_logs_output, index=False)
    
    print("\n" + "=" * 50)
    print(f"Sucesso! Gerados {len(df_logs):,} logs de atendimento.")
    print(f"Arquivo salvo em: {caminho_logs_output}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
    
    
  
    
    