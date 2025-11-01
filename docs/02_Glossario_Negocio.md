#  GLOSSÁRIO DE TERMOS E MÉTRICAS - CATÁLOGO DE COMPRAS

Este glossário define os termos de negócio e as métricas essenciais para o projeto de Ociosidade do Catálogo de Compras.

---

# 1. Glossário de Termos Six Sigma e Métricas

| Termo | Categoria | Definição no Projeto |
| :--- | :--- | :--- |
| **Métrica Y** | Métrica | **Taxa de Não-Utilização (Ociosidade):** Percentual de itens no catálogo que não foram comprados em 12 meses. |
| **Métrica X** | Causa Raiz | **Governabilidade do Item:** A qualidade do dado de governança, como a **presença e validade do Código ANVISA**. |
| **CTQ** | Cliente | **Item Válido para Compra:** Um item de catálogo que possui todos os atributos de governança (ANVISA, Fabricante, etc.) preenchidos corretamente. |
| **Baseline** | Métrica | A taxa de 70% de itens que não geraram valor (não foram comprados). |
| **COPQ** | Finanças | **Custo da Má Qualidade:** O custo administrativo de gerenciar itens obsoletos e não conformes. |

---

## 2. MÉTRICAS CHAVE DO PROCESSO (A Serem Modeladas)

| Termo | Definição | Base de Cálculo/Contexto |
| :--- | :--- | :--- |
| **Status de Utilização** | Indica se o item gerou valor. | Determinado pela presença do `id_produto` na tabela `fato_compras_medicamentos`. |
| **Compliance ANVISA** | Métrica de qualidade do cadastro. | A porcentagem de itens que possuem o campo `codigo_anvisa` preenchido e formatado corretamente. |
| **Itens Obsoletos/Inválidos** | A porção do catálogo que não deve mais ser utilizada. | Itens que não possuem o Código ANVISA preenchido (nossa Métrica X principal). |