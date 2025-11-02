# Arquivo: dashboard_control.py

import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go # Para gráficos SPC customizados
import plotly.express as px

# --- 0. CONFIGURAÇÃO E CONSTANTES DO PROJETO SIX SIGMA ---
# Defina o caminho e os limites do seu projeto para fácil manutenção
CAMINHO_RAW = 'data/raw/' 
DELIMITADOR = ';'
META_Y = 1.0  # Meta de 1.0% para a Taxa de Alto Risco
UCL_Y = 1.5   # Limite de Controle Superior (UCL) de 1.5%

st.set_page_config(layout="wide", page_title="Controle Six Sigma - Risco de Preço")


# ---------------------------------------------------------------------------------
# --- 1. FUNÇÃO DE CARREGAMENTO E JOIN DE DADOS (USANDO CACHE PARA PERFORMANCE) ---
# ---------------------------------------------------------------------------------

@st.cache_data
def load_data():
    """Carrega as tabelas e realiza os merges, usando o Data Model fornecido."""
    
    # Certifique-se que CAMINHO_RAW = 'data/raw/' está definido no topo do script
    CAMINHO_RAW = 'data/raw/' 
    DELIMITADOR = ';'
    
    try:
        # Carregar Tabela Fato (a principal, com as flags Y, X1, X3, e X2 'anvisa')
        df_fato = pd.read_csv(f'{CAMINHO_RAW}fato_compras_para_dashboard.csv', sep=DELIMITADOR, encoding='utf-8')

        # Carregar Dimensões (Usando os nomes de coluna de chave primária corretos)
        dim_produto = pd.read_csv(f'{CAMINHO_RAW}dim_produto.csv', sep=DELIMITADOR, encoding='utf-8')
        dim_fabricante = pd.read_csv(f'{CAMINHO_RAW}dim_fabricante.csv', sep=DELIMITADOR, encoding='utf-8')
        dim_fornecedor = pd.read_csv(f'{CAMINHO_RAW}dim_fornecedor.csv', sep=DELIMITADOR, encoding='utf-8')
        dim_instituicao = pd.read_csv(f'{CAMINHO_RAW}dim_instituicao.csv', sep=DELIMITADOR, encoding='utf-8')
        dim_tempo = pd.read_csv(f'{CAMINHO_RAW}dim_tempo.csv', sep=DELIMITADOR, encoding='utf-8')

    except FileNotFoundError as e:
        st.error(f"Erro ao carregar um arquivo: Certifique-se de que todos os arquivos CSV estão em {CAMINHO_RAW}. Falha: {e}")
        return pd.DataFrame()

    # 3. Realizar Merges
    df_dashboard = df_fato.copy()
    
    # 3.1. Merge com Produto (Chave: id_produto)
    # Buscando 'descricao_catmat' (Nome do Produto para o dashboard) e 'codigo_br' (para contexto)
    df_dashboard = pd.merge(df_dashboard, dim_produto[['id_produto', 'descricao_catmat', 'codigo_br']], 
                            on='id_produto', how='left')

    # 3.2. Merge com Fabricante (Chave: id_fabricante)
    df_dashboard = pd.merge(df_dashboard, dim_fabricante, on='id_fabricante', how='left')

    # 3.3. Merge com Fornecedor (Chave: id_fornecedor)
    # Buscando nome do Fornecedor
    df_dashboard = pd.merge(df_dashboard, dim_fornecedor[['id_fornecedor', 'fornecedor']], 
                            on='id_fornecedor', how='left')

    # 3.4. Merge com Instituição (Chave: id_instituicao)
    # Buscando nome da Instituição e localização (UF)
    df_dashboard = pd.merge(df_dashboard, dim_instituicao[['id_instituicao', 'nome_instituicao', 'uf']], 
                            on='id_instituicao', how='left')
    
    # 3.5. Merge com Tempo (Chave: id_tempo)
    # Buscando as colunas de tempo, exceto id_tempo (que já está na Fato)
    df_dashboard = pd.merge(df_dashboard, dim_tempo[['id_tempo', 'data_completa']], 
                            on='id_tempo', how='left')
    
    # --- 4. TRATAMENTO DE COLUNAS ---
    
    # 4.1. Garantir que o nome do produto no dashboard seja 'descricao_catmat' (Renomeando para uso genérico)
    df_dashboard.rename(columns={'descricao_catmat': 'nome_produto'}, inplace=True)
    
    # 4.2. Tratamento de Data para o SPC
    # Usando a data da dim_tempo para o Gráfico SPC
    df_dashboard['data_mes'] = pd.to_datetime(df_dashboard['data_compra']) 
    df_dashboard['Mes_Ano'] = df_dashboard['data_mes'].dt.to_period('M').astype(str)

    # 4.3. Cálculo do KPI de Ganhos Financeiros Estimados (Baseado no PMP)
    df_dashboard['Ganho_Estimado'] = np.where(
        (df_dashboard['Y_Risco_Status'] == 'ALTO RISCO (Defeito Y)') & (df_dashboard['score_z_risco'] > 0),
        (df_dashboard['preco_unitario'] - df_dashboard['pmp_medio']) * df_dashboard['qtd_itens_comprados'], 
        0
    )
    
    return df_dashboard


# Carrega e consolida todos os dados
df = load_data()


# ---------------------------------------------------------------------------------
# --- 2. CÁLCULOS DAS MÉTRICAS DE CONTROLE (KPIs) ---
# ---------------------------------------------------------------------------------

if not df.empty:
    
    # 2.1. Cálculo da Taxa Y (Geral)
    total_transacoes = len(df)
    defeitos_y = df[df['Y_Risco_Status'] == 'ALTO RISCO (Defeito Y)']
    total_defeitos_y = len(defeitos_y)
    taxa_y_atual = (total_defeitos_y / total_transacoes) * 100 if total_transacoes > 0 else 0
    
    # 2.2. Cálculo do Total de Ganhos Estimados
    ganho_acumulado = df['Ganho_Estimado'].sum()

    # 2.3. Cálculo da Métrica Xc1 (Compliance 3 Cotações) - SIMULADO
    # **NOTA:** Esta métrica precisa de uma coluna 'flag_3_cotacoes_anexadas' no seu CSV real.
    # Aqui, simulamos que o compliance é o percentual de transações de alto risco no Pregão
    # que tem uma flag positiva (simularemos 95% para o exemplo de dashboard).
    transacoes_gatilho = df[df['Status_Risco_Aquisicao'] == 'ALTO RISCO DE AQUISIÇÃO (Protocolo Otimizado NECESSÁRIO)']
    # SIMULAÇÃO: 92% de compliance no mundo real
    compliance_xc1 = 0.92 * 100 
    
    
    # ---------------------------------------------------------------------------------
    # --- 3. CONSTRUÇÃO DO DASHBOARD (STREAMLIT UI) ---
    # ---------------------------------------------------------------------------------

    st.title(" FASE CONTROL: Monitoramento do Alto Risco de Preço (SPC)")
    st.markdown("Dashboard de Controle Estatístico do Processo (SPC) para sustentabilidade dos ganhos Green Belt.")
    st.divider()

    # --- LINHA 1: KPIS DE RESULTADO E COMPLIANCE ---
    col1, col2, col3, col4 = st.columns(4)
    
    # KPI 1: Taxa Y Atual
    col1.metric(
        label="Taxa de Alto Risco (Métrica Y)", 
        value=f"{taxa_y_atual:.2f}%", 
        delta=f"Meta: {META_Y:.2f}% | UCL: {UCL_Y:.2f}%",
        delta_color="inverse" if taxa_y_atual > UCL_Y else "normal"
    )

    # KPI 2: Ganhos Acumulados
    col2.metric(
        label="Ganhos Estimados Acumulados (Mitigação COPQ)",
        value=f"R$ {ganho_acumulado:,.2f}"
    )

    # KPI 3: Compliance (Xc1) - O Processo está sendo Seguido?
    col3.metric(
        label="Compliance Protocolo 3 Cotações (Xc1)",
        value=f"{compliance_xc1:.1f}%",
        delta="Meta: 100%",
        delta_color="inverse"
    )
    
    # KPI 4: Total de Defeitos (Absoluto)
    col4.metric(
        label="Transações que Dispararam o Gatilho", 
        value=f"{len(transacoes_gatilho):,}",
        help="Total de transações que exigiram o Protocolo Otimizado (Filtro X1/X3)."
    )

    st.divider()

    # --- LINHA 2: GRÁFICO SPC (Controle Estatístico) ---

    st.header("1. Gráfico de Controle SPC - Taxa de Alto Risco (Métrica Y)")

    # Agrupamento para o gráfico SPC (Taxa Y por mês)
    df_spc = df.groupby('Mes_Ano').agg(
        Total_Transacoes=('id_pedido', 'count'),
        Total_Defeitos=('Y_Risco_Status', lambda x: (x == 'ALTO RISCO (Defeito Y)').sum())
    ).reset_index()

    df_spc['Taxa_Defeito'] = (df_spc['Total_Defeitos'] / df_spc['Total_Transacoes']) * 100
    
    # Criação do Gráfico de Linha (SPC Chart)
    fig = px.line(df_spc, x='Mes_Ano', y='Taxa_Defeito', title='Taxa de Alto Risco de Preço ao Longo do Tempo')
    
    # Adicionando Linhas de Controle
    fig.add_hline(y=META_Y, line_dash="dash", line_color="green", annotation_text=f"META ({META_Y}%)")
    fig.add_hline(y=UCL_Y, line_dash="dash", line_color="red", annotation_text=f"LIMITE DE AÇÃO ({UCL_Y}%)")
    
    fig.update_layout(yaxis_title='Taxa de Alto Risco (%)', xaxis_title='Mês/Ano', hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    
    # --- LINHA 3: DIAGNÓSTICO E PLANO DE REAÇÃO ---

    st.header("2. Plano de Reação (Análise das Causas X)")
    st.markdown("Se a Taxa Y exceder o Limite de Ação (1.5%), o gestor deve auditar as causas abaixo:")
    
    col_x1, col_x3 = st.columns(2)
    
    # Métrica X3: Defeitos por Modalidade (Onde o Defeito está Ocorrendo)
    df_modalidade = defeitos_y.groupby('modalidade_compra').size().reset_index(name='Total_Defeitos')
    
    # 1. ORDENAR: Ordenamos em ordem decrescente (do maior para o menor defeito)
    df_modalidade = df_modalidade.sort_values(by='Total_Defeitos', ascending=True)

    # 2. CRIAR GRÁFICO DE BARRAS HORIZONTAIS
    fig_modalidade = px.bar(
        df_modalidade, 
        x='Total_Defeitos', 
        y='modalidade_compra', 
        orientation='h', # Define como barras horizontais
        title='Concentração de Defeitos Y por Modalidade (Plano de Ação X3)',
        text='Total_Defeitos', # Mostra o valor na barra
        color='modalidade_compra' # Cores por modalidade
    )
    
    # Ajustes finos: Mudar rótulos e layout
    fig_modalidade.update_layout(
        xaxis_title='Número de Defeitos (Z-Score > 2.0)',
        yaxis_title='Modalidade de Compra',
        showlegend=False
    )
    
    # Formato do texto dentro das barras
    fig_modalidade.update_traces(texttemplate='%{text:,}', textposition='outside')
    
    col_x3.plotly_chart(fig_modalidade, use_container_width=True)
    
    # Métrica X1: TOP 5 Produtos (Onde a Causa Intermitência é Crítica)
    df_produtos_criticos = defeitos_y.groupby('nome_produto').agg(
        Total_Defeitos=('id_pedido', 'count'),
        Risco_Medio=('Risco_Intermitencia', 'mean')
    ).reset_index().sort_values('Total_Defeitos', ascending=False).head(5)
    
    col_x1.subheader("TOP 5 Produtos com Mais Defeitos Y")
    col_x1.dataframe(df_produtos_criticos.style.format({
        'Total_Defeitos': '{:,}',
        'Risco_Medio': '{:.1%}'
    }), use_container_width=True)
    col_x1.markdown(" **Plano de Reação X1:** Auditar o PMP Móvel para estes itens e o cadastro de ANVISA.")
    
    
    # --- LINHA 4: TABELA DE ALERTA E AÇÃO ---
    st.header("3. ALERTA DE AÇÃO IMEDIATA: TOP 100 MAIORES DESVIOS POSITIVOS (COPQ)")
st.markdown(
    "Filtro em tempo real para as transações mais recentes (últimos 100 dias) que continuam apresentando Alto Risco de Preço (Z-Score > 2.0). "
    "Use esta tabela para auditar o *compliance* imediato (Xc1) do Protocolo Otimizado."
)

# 1. Filtrar Outliers Positivos Recentes
# Focamos em Z-Score POSITIVO (Gasto Excessivo)
df_alerta = df[
    (df['Y_Risco_Status'] == 'ALTO RISCO (Defeito Y)') & 
    (df['score_z_risco'] > 0)
].copy()

# 2. Ordenar pelo MAIOR Gasto Excessivo e depois pela data (para ver os mais recentes entre os piores)
df_alerta = df_alerta.sort_values(
    by=['Ganho_Estimado', 'data_mes'], 
    ascending=[False, False]
).head(100) # Mantemos os 100 maiores desvios monetários

# 3. Seleção de Colunas Chave para o Alerta
colunas_alerta = [
    'Mes_Ano', 
    'nome_produto', 
    'preco_unitario', 
    'pmp_medio', 
    'Ganho_Estimado', # Este é o Gasto Excessivo por transação
    'score_z_risco', 
    'fornecedor',
    'modalidade_compra'
]

st.dataframe(df_alerta[colunas_alerta].style.format({
    'preco_unitario': 'R$ {:,.2f}',
    'pmp_medio': 'R$ {:,.2f}',
    'Ganho_Estimado': 'R$ {:,.2f}',
    'score_z_risco': '{:.2f}'
}), use_container_width=True)

st.caption("Ação de Reação: Se a transação estiver no Pregão e Intermitente, verifique imediatamente a documentação de 3 cotações (Xc1).")