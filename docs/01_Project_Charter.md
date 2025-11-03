## PROJECT CHARTER: MITIGAÇÃO DO ALTO RISCO DE PREÇO NO PROCESSO DE COMPRAS PÚBLICAS DE MEDICAMENTOS (Ênfase no Pregão)

### 1. INFORMAÇÕES BÁSICAS

| Título do Projeto | Otimização do Processo de Compras: Mitigação do Alto Risco de Preço em Itens Intermitentes. |
| :--- | :--- |
| Metodologia | Lean Six Sigma (Green Belt) |
| Líder do Projeto | DEBORA REBULA KLEIN (Consultor/Analista de Dados) |
| Início Previsto | 31/10/2025 |
| Duração Estimada | 4 a 6 Meses |
| Origem dos Dados | datasus.saude.gov.br/dataset/bps |
| Período Analisado | 2020 a 2025 |

---

### 2. FASE DEFINE: DECLARAÇÃO DO PROBLEMA E OBJETIVO

#### 2.1. Declaração do Problema (As Perdas - Métrica Y)

O processo de aquisição de medicamentos apresenta um alto índice de transações com **preços atípicos (outliers)**, indicando instabilidade no *benchmarking* de preços e **risco de gasto excessivo (COPQ)**, sendo este problema concentrado em itens comprados esporadicamente.

* **Problema Quantificado (Y - BASELINE):** $\mathbf{2.50%}$ das $\mathbf{263.562}$ transações de compra estão em Alto Risco de Preço (Z-Score $|>2.0|$).
* **Causa Raiz Comprovada (X):** $\mathbf{100\%}$ desses defeitos ocorrem em produtos com **Intermitência Média/Alta** e $83.18\%$ deles na modalidade **Pregão**.

#### 2.2. Objetivo do Projeto (Melhoria SMART)

O objetivo é atuar nas Causas Raízes (X) para reduzir a variabilidade e o risco de gasto excessivo.

| Critério | Objetivo |
| :--- | :--- |
| **Specific (Específico)** | Implementar o **Protocolo de Sourcing Otimizado** para itens intermitentes na modalidade Pregão. |
| **Measurable (Mensurável)** | Reduzir o Baseline de Alto Risco de $\mathbf{2.50\%}$ para um máximo de $\mathbf{1.0\%}$ do total de transações. |
| **Achievable (Alcançável)** | Focar a melhoria no subconjunto de $\mathbf{5.894}$ transações que atende o critério de **Alto Risco de Aquisição**. |
| **Relevant (Relevante)** | Reduzir o risco de gasto excessivo (COPQ) e aumentar a confiabilidade do PMP de referência. |
| **Time-bound (Prazo)** | O objetivo primário deve ser alcançado em $\mathbf{6 \text{ meses}}$ após a implementação do novo protocolo. |

---

### 3. FASE ANALYZE: CONCLUSÃO DO DIAGNÓSTICO (A Evidência)

A análise dos $\mathbf{6.575}$ defeitos (Alto Risco) demonstrou a necessidade de focar o *IMPROVE* na fragilidade do PMP de itens irregulares.

| Causa Raiz | Métrica de Foco | Diagnóstico para o IMPROVE |
| :--- | :--- | :--- |
| **X1 - Risco de Intermitência** | $\mathbf{100\%}$ dos defeitos (Y) | O PMP histórico é volátil; será substituído pelo **PMP Móvel (6 meses)** (Ação A2). |
| **X3 - Modalidade Pregão** | $\mathbf{83.18\%}$ dos defeitos (Y) | O processo de compra precisa de **validação externa (3 Cotações)** para itens críticos (Ação A1). |
| **X2 - Qualidade de Dados** | Secundário (Ação Poka-Yoke) | Será implementado um *hard stop* (Poka-Yoke) para bloquear a compra de itens críticos sem o Código ANVISA preenchido (Ação A4). |

---

### 4. ESCOPO DO PROJETO (O Que Será e o Que Não Será Feito)

| Incluído | Excluído |
| :--- | :--- |
| **Análise do Risco de Intermitência (X1) e do Z-Score (Y) para todos os itens da base de compras.** | Otimização do processo de logística de entrega dos medicamentos. |
| **Criação e implementação de um Protocolo de Sourcing Diferenciado (PMP Móvel e 3 Cotações) para itens intermitentes negociados via Pregão.** | Negociação direta de preços com fornecedores (o foco é no processo, não na negociação em si). |
| **Criação de um Painel de Controle (Dashboard) para monitoramento contínuo (FASE CONTROL).** | Análise da variação de preços de itens de compra **regular** (Intermitência Baixa). |
