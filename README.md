
#  PROJETO GREEN BELT: MITIGAÇÃO DO ALTO RISCO DE PREÇO EM COMPRAS PÚBLICAS

Este repositório documenta a aplicação da metodologia Lean Six Sigma (Green Belt) em um desafio estratégico: a **mitigação do Alto Risco de Preço (Outliers)** em aquisições de medicamentos, um problema que ameaça a eficiência do gasto público.

**Metodologia:** DMAIC - Definir, Medir, Analisar, Melhorar, Controlar.
**Foco:** Otimização do protocolo de Sourcing no Pregão para itens com demanda instável (Intermitência).

---

## 1. FASE DEFINE (O Escopo e a Métrica de Sucesso)

O problema foi formalmente redefinido com base no valor financeiro e na variabilidade do processo (Defeito Y).

| Métrica Chave | Definição | Baseline Comprovado | Meta SMART |
| :--- | :--- | :--- | :--- |
| **Métrica Y** (Defeito) | Taxa de Transações com Alto Risco de Preço (Z-Score $>2.0$). | **2.50%** (de 263.562 transações). | Redução para um máximo de **1.0%** (em 6 meses). |
| **Dano (COPQ)** | Risco de Gasto Excessivo. | Casos críticos com desvios de Z-Score de até $\mathbf{17.34}$. | Mitigação de $\mathbf{60\%}$ do risco no processo de compra. |

### [ACESSAR O PROJECT CHARTER COMPLETO (docs/01_Project_Charter.md)]

---

## 2. FASE MEASURE & ANALYZE (O Diagnóstico da Causa Raiz)

A análise estatística comprovou que o problema é sistêmico e não aleatório, concentrando-se na interseção de duas causas raízes:

###  Prova de Concentração (Regra 80/20)

| Causa Raiz (X) | Impacto Comprovado | Implicação no Processo |
| :--- | :--- | :--- |
| **X1: Risco de Intermitência** | $\mathbf{100\%}$ dos Defeitos (Y) | O PMP (Preço Médio) de referência é volátil e falho para estes itens. |
| **X3: Modalidade Pregão** | $\mathbf{83.18\%}$ dos Defeitos (Y) | O protocolo de *sourcing* é insuficiente para garantir o preço justo em compras críticas. |

###  Amostra dos Outliers Positivos (Evidência do Dano)

A tabela a seguir apresenta os maiores desvios de preço, comprovando o Gasto Excessivo em itens intermitentes, principalmente no Pregão:

| ID Produto | Modalidade | Intermitência (X1) | Preço Pago (Y) | PMP Médio Ref. | Z-Score Risco |
|:---|:---|:---|:---|:---|---:|
| Pro00485 | Dispensa de Licitação | 46.2% | R$ 195.43 | R$ 3.50 | 17.34 |
| Pro00175 | Pregão | 47.7% | R$ 302.50 | R$ 5.73 | 16.37 |
| Pro07282 | Pregão | 81.5% | R$ 3,072.00 | R$ 39.52 | 16.07 |
| Pro00097 | Pregão | 44.6% | R$ 73.86 | R$ 0.49 | 15.17 |
| Pro07441 | Pregão | 70.8% | R$ 6,000.00 | R$ 29.69 | 14.46 |

---

## 3. FASE IMPROVE & CONTROL (A Solução e a Sustentabilidade)

### FASE IMPROVE: Protocolo de Sourcing Otimizado

A solução é a implementação de um **Protocolo Otimizado (Ações A1/A2)**, ativado por um **Gatilho de Risco** que mira apenas nas transações mais críticas.

| Ação de Melhoria | Alvo (Causa X) | Entregável de Processo |
| :--- | :--- | :--- |
| **A1. 3 Cotações Obrigatórias** | X3 (Pregão) | Exigir validação externa de preço para o Alto Risco. |
| **A2. PMP Móvel (6 Meses)** | X1 (Intermitência) | Substituir o *benchmark* volátil por um PMP mais recente e estável. |
| **A4. Poka-Yoke de Governança** | X2 (Dados) | Bloquear a aprovação de itens de Alto Risco sem o Código ANVISA. |

> **Foco Estratégico (Lean):** O novo protocolo será aplicado APENAS nas **5.894 transações** que cumprem o critério de Alto Risco de Aquisição, maximizando o impacto com esforço mínimo ($\mathbf{2.24\%}$ do universo total).

### FASE CONTROL: Monitoramento Estatístico (SPC)

O sucesso e a sustentabilidade das ações são garantidos pelo monitoramento contínuo das métricas de processo e de resultado em um Dashboard de Controle.

| Métrica Monitorada | Tipo de Métrica | Limite de Controle (UCL) |
| :--- | :--- | :--- |
| **Taxa de Alto Risco (Y)** | Resultado | $\mathbf{1.5\%}$ (Dispara Auditoria e Ação de Reação). |
| **Compliance 3 Cotações (Xc1)** | Processo | $\mathbf{90\%}$ (Abaixo disso, exige Treinamento de Reforço). |