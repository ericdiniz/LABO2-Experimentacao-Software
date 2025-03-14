# Relatório - Lab02S01: Coleta de Repositórios Java

## 1. Introdução

Este relatório apresenta a primeira etapa do **Laboratório 02** – "Um estudo das características de qualidade de sistemas Java". Nesta fase, realizamos a coleta dos **1.000 repositórios Java mais populares** do GitHub, com base na contagem de estrelas (_stars_), e armazenamos os dados em um arquivo **CSV**.

A coleta de dados foi feita utilizando a **API GraphQL do GitHub**, garantindo um processo eficiente e escalável para extrair informações detalhadas dos repositórios.

---

## 2. Metodologia

A metodologia utilizada para a extração dos repositórios seguiu os seguintes passos:

1. **Definição da Query GraphQL**
   - Criamos uma consulta GraphQL para buscar os repositórios **mais populares** escritos em **Java**, ordenando pelos repositórios com **maior número de estrelas**.
2. **Uso da API do GitHub**

   - Utilizamos a API do GitHub para coletar informações dos repositórios, incluindo:
     - Nome do repositório
     - Quantidade de estrelas (_stargazers_count_)
     - Quantidade de _forks_
     - URL do repositório

3. **Automação do Processo**
   - Criamos um **script em Python** para realizar a coleta de forma automatizada, iterando sobre as páginas de resultados até atingir **1.000 repositórios**.
   - O script armazena os dados coletados em um **arquivo CSV** para facilitar a análise posterior.

---

## 3. Resultados Obtidos

Após a execução do script, obtivemos um total de **1.000 repositórios Java**, contendo os seguintes dados:

O arquivo **`repositories.csv`** contém todas as informações coletadas e será usado para a próxima fase do laboratório.

---

## 4. Conclusão

A primeira fase do **Laboratório 02** foi concluída com sucesso, garantindo a coleta dos **1.000 repositórios Java mais populares** do GitHub. Esses dados servirão como base para a análise de métricas de qualidade na próxima etapa do estudo.

---
