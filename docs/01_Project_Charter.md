#  PROJECT CHARTER: Otimização do Atendimento e Capacidade do Hospital SCQM

## 1. INFORMAÇÕES BÁSICAS

| Título do Projeto | Otimização do Tempo de Espera (Lead Time) e Aumento da Capacidade de Atendimento no Ambulatório. |
| :--- | :--- |
| **Metodologia** | Lean Six Sigma (Green Belt) |
| **Patrocinador (Sponsor)** | Grupo de Investidores (Stakeholders que detêm o capital) |
| **Líder do Projeto** | DEBORA REBULA KLEIN (Consultor/Engenheiro de Dados) |
| **Início Previsto** | 31/10/2025 |
| **Duração Estimada** | 4 a 6 Meses |

---

## 2. FASE DEFINE: DECLARAÇÃO DO PROBLEMA E OBJETIVO

### 2.1. Declaração do Problema (As Perdas)

O Hospital Santa Casa de Quem Grita Mais enfrenta uma grave crise financeira e perda de clientes devido à ineficiência operacional no atendimento ambulatorial.

* **Problema Quantificado:** O Tempo Médio de Espera é de **4 horas**, com picos de **8 horas**.
* **Consequência:** Perda de receita potencial, alta evasão de pacientes, má reputação e desconforto generalizado (lotação da sala de espera, que tem capacidade para 10, mas recebe mais de 20).
* **Receita Perdida Estimada:** O concorrente atende 360 pacientes/dia. Com a mesma equipe, o SCQM atende 160. A perda de receita potencial é de **200 pacientes/dia** (200 x R$ 100,00) = **R$ 20.000,00/dia**.

### 2.2. Objetivo SMART (A Solução)

O objetivo é atuar nas causas raízes da alta variabilidade e do descontrole do processo.

| Critério | Objetivo |
| :--- | :--- |
| **S**pecific (Específico) | Reduzir o **Tempo Médio de Espera do Paciente (Lead Time)**. |
| **M**easurable (Mensurável) | Reduzir o **Tempo Médio de Espera de 4h para menos de 60 minutos (1 hora)**. |
| **A**chievable (Alcançável) | Aumentar o Volume Médio de Atendimento de 160 para **250 pacientes/dia**. |
| **R**elevant (Relevante) | Reverter a crise financeira e aumentar a satisfação do cliente. |
| **T**ime-bound (Prazo) | O objetivo primário deve ser alcançado em 4 meses. |

---

## 3. ESCOPO DO PROJETO (O Que Será e o Que Não Será Feito)

| Incluído | Excluído |
| :--- | :--- |
|  Processo de **Agendamento, Recepção e Espera** do Ambulatório. |  Otimização de Processos Cirúrgicos ou Internação. |
|  Análise da **Variabilidade do Tempo de Atendimento** por Médico. |  Compra ou Troca de Sistemas de Agendamento (Foco na otimização do processo atual). |
|  Criação de um **Sistema de Controle Estatístico** (Dashboard MiniPy). |  Treinamento de Soft Skills para Atendentes ou Médicos. |

---

## 4. ESTRATÉGIA DE DADOS E ENGENHARIA

O diferencial do projeto será a automação das análises estatísticas do Six Sigma.

* **Métrica Y (a ser modelada):** Tempo de Espera (minutos).
* **Fontes de Dados Críticas:** Logs do sistema de *Check-in/Check-out*, Registros de Início/Fim da Consulta, Escala Médica.
* **Entregável Central de Engenharia:** **Framework "MiniPy"** (Dashboard em Streamlit) para monitorar as Métricas de Controle (LSC/LIC) em tempo real.