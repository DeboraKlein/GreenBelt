#  GLOSSÁRIO DE TERMOS E MÉTRICAS INICIAIS

Este glossário define os termos de negócio e as métricas essenciais que serão utilizadas para medir, analisar e controlar o processo de atendimento do Hospital Santa Casa de Quem Grita Mais.

---

## 1. MÉTRICAS CHAVE DO PROCESSO (A Serem Modeladas)

| Termo | Definição | Base de Cálculo/Contexto |
| :--- | :--- | :--- |
| **Tempo de Espera (Lead Time)** | O tempo que um paciente gasta desde o **Check-in na Recepção** até o **Início Efetivo da Consulta**. (A principal métrica Y). | `Início da Consulta (Log) - Check-in (Log)` |
| **Tempo de Ciclo (Cycle Time)** | O tempo total que o Médico gasta no atendimento de uma única consulta. | `Fim da Consulta (Log) - Início da Consulta (Log)` (Apresenta alta variabilidade: 5 a 50 minutos). |
| **Taxa de Evasão (Perda)** | Percentual de pacientes que desistem da espera e vão embora sem atendimento. | `(Pacientes que Desistiram / Total de Pacientes que Fizeram Check-in) * 100` |
| **Capacidade Ociosa** | A diferença entre a capacidade de atendimento atual (160/dia) e a capacidade máxima (aproximadamente 360/dia, baseada no concorrente). | `360 - 160 = 200 pacientes/dia de potencial não atendido` |
| **Custo da Má Qualidade (COPQ)** | A receita perdida devido à evasão e à incapacidade de atender mais pacientes. | `(Pacientes Perdidos Diariamente) * R$ 100,00` |

---

## 2. TERMOS DE GOVERNANÇA E SEIS SIGMA

| Termo | Definição | Contexto no Projeto |
| :--- | :--- | :--- |
| **Variabilidade** | As oscilações no tempo de ciclo e de espera (ex: de 5 a 50 minutos). A principal causa do descontrole. | O projeto visa **reduzir a variabilidade** para garantir um tempo de espera previsível (estável). |
| **Fora de Controle Estatístico** | Uma métrica que ultrapassa os limites de controle (LSC/LIC) em um Gráfico de Controle. | Aplicável aos Médicos que sistematicamente gastam 50 minutos ou chegam atrasados, sendo *outliers* na análise. |
| **Gargalo (Bottleneck)** | O ponto do processo que limita a saída total. | A alta variabilidade do tempo de ciclo e a falta de padronização no agendamento são os gargalos do SCQM. |
| **MiniPy** | O framework de análise estatística em Python/Streamlit criado para este projeto. | Ferramenta de **Controle** que automatizará os Gráficos de Controle do DMAIC. |