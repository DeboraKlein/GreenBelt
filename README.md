
## 1. FASE DEFINE (O Escopo Estratégico)

O problema foi formalmente redefinido e focado em valor financeiro, abandonando a métrica inicial de Ociosidade.

| Métrica Chave | Definição | Baseline Comprovado | Meta SMART (6 Meses) |
| :--- | :--- | :--- | :--- |
| **Métrica Y (Risco de Preço)** | Taxa de Transações de Compra com Z-Score $|>2.0|$ (Alto Risco de Preço). | **2.50%** de 263.562 transações. | Redução para um máximo de **1.0%**. |
| **Dano (COPQ)** | Risco de Gasto Excessivo Não-Justificado. | Casos críticos com Z-Score de até $17.34$. | Mitigação de $\mathbf{60\%}$ do risco. |

### [ACESSAR O PROJECT CHARTER COMPLETO (docs/01_Project_Charter.md)]

---

## 2. FASE MEASURE & ANALYZE (O Diagnóstico Estatístico)

O universo de $\mathbf{263.562}$ transações foi analisado, confirmando a concentração do defeito em duas causas raízes:

| Causa Raiz | Impacto Comprovado | Ação de Melhoria (IMPROVE) |
| :--- | :--- | :--- |
| **X1: Risco de Intermitência** | $\mathbf{100\%}$ dos Defeitos (Y) ocorrem em produtos com Intermitência Média/Alta. | Implementar o uso de **PMP Móvel (6 meses)**. |
| **X3: Modalidade Pregão** | $\mathbf{83.18\%}$ dos Defeitos (Y) ocorrem na modalidade Pregão. | Implementar o **Protocolo de Sourcing Otimizado (3 Cotações)**. |

### Evidência Crítica: Amostra dos Outliers Positivos (Dano Financeiro)

A tabela abaixo exibe os maiores desvios de preço, comprovando o falho *benchmarking* para itens intermitentes negociados no Pregão:

| ID Produto | Modalidade | Intermitência (X1) | Preço Pago (Y) | PMP Médio Ref. | Z-Score Risco |
|:---|:---|:---|:---|:---|---:|
| Pro00485 | Dispensa de Licitação | 46.2% | R$ 195.43 | R$ 3.50 | 17.34 |
| Pro00175 | Pregão | 47.7% | R$ 302.50 | R$ 5.73 | 16.37 |
| Pro07282 | Pregão | 81.5% | R$ 3,072.00 | R$ 39.52 | 16.07 |
| Pro00097 | Pregão | 44.6% | R$ 73.86 | R$ 0.49 | 15.17 |
| Pro07441 | Pregão | 70.8% | R$ 6,000.00 | R$ 29.69 | 14.46 |

---

## 3. FASE IMPROVE & CONTROL (A Solução e Sustentabilidade)

### Foco Estratégico (O Gatilho da Ação)

A solução será implementada de forma *Lean*, ativando o **Protocolo Otimizado** (3 Cotações e PMP Móvel) APENAS para as **5.894 transações** que se enquadram na zona de "Alto Risco de Aquisição" (Defeito Y + Causas X1/X3).

### Controle Estatístico (SPC)

O sucesso será monitorado por um **Dashboard de Controle** com foco em:

| Métrica de Processo | Limite de Controle (Meta) | Ação Corretiva (UCL) |
| :--- | :--- | :--- |
| **Métrica Y (Taxa de Alto Risco)** | $\mathbf{1.0\%}$ | Auditoria se atingir $\mathbf{1.5\%}$ por 2 meses. |
| **Compliance 3 Cotações** | $100\%$ | Treinamento de reforço para compradores se cair abaixo de $90\%$. |
| **Uso de PMP Móvel** | $100\%$ | Revisão da regra de cálculo da Intermitência. |