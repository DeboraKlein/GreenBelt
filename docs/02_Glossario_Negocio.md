## GLOSSÁRIO DE TERMOS E MÉTRICAS - PROJETO GREEN BELT: MITIGAÇÃO DE RISCO DE PREÇO

Este glossário define os termos de negócio e as métricas essenciais para o projeto Green Belt, focado na mitigação da instabilidade e do Alto Risco de Preço nas compras de medicamentos.

| Termo | Categoria | Definição no Projeto |
| :--- | :--- | :--- |
| **Métrica Y** | Métrica de Resultado | **Taxa de Transações com Alto Risco de Preço:** Percentual de transações onde o preço pago se desvia significativamente do PMP. (Medido por Z-Score $|>2.0|$). |
| **Z-Score Risco** | Métrica Estatística | **Score de Desvio Padrão:** Medida de quão longe o preço unitário da transação está do PMP Médio. Usado como o critério estatístico para identificar o Defeito Y. |
| **Causa Raiz Dominante (X1)** | Causa Raiz | **Risco de Intermitência:** A instabilidade na demanda de um produto, medida pela frequência de compra (Meses Comprados / Período Total). A Causa Raiz Primária do Defeito Y. |
| **Local do Defeito (X3)** | Causa Raiz | **Modalidade Pregão:** A modalidade de compra que concentra a maior parte dos defeitos de Alto Risco de Preço, sendo o foco do *IMPROVE*. |
| **CTQ** | Cliente | **Preço Unitário Estável e Justo:** Um preço pago na transação que não é um *outlier* estatístico (Z-Score $\leq 2.0$) e que reflete o valor de mercado. |
| **Baseline** | Métrica | A taxa inicial de **2.50%** de transações que apresentam Alto Risco de Preço (Gasto Excessivo ou Preço Atípico). |
| **COPQ** | Finanças | **Custo da Má Qualidade (Gasto Excessivo):** O valor monetário total potencialmente gasto acima do PMP médio de referência nas transações com Z-Score Positivo. |
| **PMP Médio** | Benchmarking | **Preço Médio Ponderado Histórico:** Média de preço usada como *benchmark* de referência antes do projeto (considerado falho para X1). |
| **PMP Móvel (6 Meses)** | Ação de Melhoria (A2) | **Novo *Benchmark* Otimizado:** O PMP calculado usando apenas as compras dos últimos 6 meses, implementado para itens com Intermitência Média/Alta. |
| **Protocolo Otimizado** | Ação de Melhoria (A1) | O conjunto de novas regras (Exigência de 3 Cotações) ativado para as transações classificadas como **Alto Risco de Aquisição**. |
| **Gatekeeping** | Processo / IT | **Ponto de Controle no Sistema:** Implementação de uma barreira ou *hard stop* que exige a validação de dados ou ações (Poka-Yoke) antes da aprovação final da compra. |
| **Poka-Yoke (Ação A4)** | Control | **À Prova de Erro:** O bloqueio da transação de Alto Risco se o Código ANVISA estiver faltando, prevenindo que o defeito (Y) ocorra sob condições de má governança (X2). |
| **Taxa de Compliance** | Métrica de Processo | **Métricas Xc1 e Xc2:** O percentual de adesão às novas regras do Protocolo Otimizado (ex: % de Pregões de Alto Risco que, de fato, tiveram 3 cotações). |
