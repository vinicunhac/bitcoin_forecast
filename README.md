# **Predicting Bitcoin Prices with LSTM**

## **Introdução**

Este documento fornece uma visão geral do uso de modelos de Long Short-Term Memory (LSTM) para prever preços do Bitcoin.

## **Visão Geral do Bitcoin**

Bitcoin é uma moeda digital descentralizada, sem um banco central ou administrador único, que pode ser transferida na rede ponto a ponto sem intermediários.

## **Explicação do Modelo**

LSTM é um tipo de rede neural recorrente (RNN) capaz de aprender dependências de ordem em problemas de previsão de sequências. É projetado para funcionar com sequências de dados, tornando-o ideal para previsões de séries temporais como os preços do Bitcoin. A vantagem do LSTM em relação às redes neurais tradicionais neste contexto é a capacidade de lembrar entradas anteriores por um longo período, captando tendências e padrões no comportamento dos preços das criptomoedas.

### **Arquitetura do Modelo**

* **Camadas LSTM**: Utilizamos duas camadas LSTM para capturar tanto a dependência de curto prazo quanto a de longo prazo nas séries temporais. A função de ativação ‘ReLU’ é usada para introduzir não linearidade.

* **Camadas Dropout**: Aplicamos camadas dropout após as camadas LSTM para evitar o overfitting, com uma taxa de descarte de 20%.

* **Camada Densa**: Uma camada densa no final para prever o valor de saída com base nos aprendizados das camadas LSTM.

### **Hiperparâmetros Utilizados**

* **Unidades**: O número de neurônios em cada camada LSTM, que determina a capacidade do modelo de aprender padrões. Usamos 100 unidades em cada camada LSTM.

* **Função de Ativação**: A função ‘ReLU’ é escolhida por sua capacidade de lidar bem com problemas de gradiente.

* **Dropout**: Configurado em 20%, para desligar aleatoriamente 20% das unidades durante o treinamento, ajudando na generalização.

* **Tamanho do Lote (Batch Size)**: Determina o número de amostras por atualização de gradiente. Influencia na convergência do modelo.

* **Épocas (Epochs)**: O número de passagens completas através do conjunto de dados de treinamento, configurado em 150 para garantir que o modelo aprenda adequadamente.

* **Otimização**: O algoritmo ‘Adam’ é usado por sua eficiência com grandes conjuntos de dados e gradientes esparsos.

* **Função de Perda**: O Erro Quadrático Médio (MSE) é utilizado para medir a precisão das previsões do modelo.

## **Fonte de Dados**

Os dados históricos do Bitcoin são provenientes da Alpha Vantage, uma plataforma que oferece dados em tempo real e históricos sobre criptomoedas e outros instrumentos financeiros. O conjunto de dados cobre registros de 15 de março de 2023 até 16 de março de 2023, com um total de 2 registros. Inclui características essenciais como preços de abertura, alta, baixa, fechamento diário e volume para preparar o conjunto de dados para o treinamento do modelo.

## **Visualização do Dashboard**

O projeto inclui um dashboard baseado em Gradio que visualiza os dados históricos e as previsões de preços futuros do Bitcoin. Esta interface interativa fornece aos usuários gráficos dinâmicos, mostrando tendências de dados passados e movimentos de preços previstos para os próximos dias, permitindo uma melhor tomada de decisão baseada em dados.

## **Utilização do Modelo**

As redes LSTM são particularmente benéficas ao lidar com longas sequências de dados com dependências temporais. Elas ajudam a modelar relações complexas não lineares muitas vezes encontradas em dados de séries temporais, como preços de criptomoedas, captando padrões enterrados dentro de dados históricos. Essa característica torna o LSTM uma escolha preferida para previsões financeiras.

## **Conclusão**

Usar redes LSTM para previsão de preços do Bitcoin permite capturar dependências temporais cruciais para previsões precisas no volátil mercado de criptomoedas. Sua arquitetura as torna adequadas para lidar de forma eficaz com dados sequenciais, permanecendo uma ferramenta eficiente em aplicações de previsão. Atualizações contínuas do modelo e ajustes finos são essenciais para manter a precisão, dada a natureza dinâmica do mercado.