📊 Previsão de Evasão Escolar / Universitária
Projeto Prático de Mineração de Dados (PP)

Este projeto tem como objetivo desenvolver uma solução baseada em dados para identificar alunos com risco de abandonar o curso. Utilizando técnicas de Machine Learning, o modelo busca prever a evasão com base em variáveis acadêmicas e socioeconômicas, permitindo intervenções preventivas.
👥 Integrantes do Grupo

    Fabíola Nascimento

    Iago Faria

    Maria Luiza

    Paulo Otávio

🚀 Como Executar o Projeto

O código completo, incluindo a geração dos dados, análise exploratória e modelagem, está disponível para execução online através do Google Colab. Não é necessária instalação local.

Link direto: [Acessar Notebook no Google Colab](https://colab.research.google.com/drive/1ANJADZQgE3wiwD92rr7N5bnHmp9VRibJ?usp=sharing)


📋 Estrutura do Projeto

O desenvolvimento seguiu o fluxo padrão de Mineração de Dados (KDD/CRISP-DM), atendendo aos requisitos da disciplina:

    Descrição do Problema: Evasão escolar e seus impactos.

    ETL (Extração, Transformação e Carga):

        Geração/Carga de dados.

        Tratamento de variáveis (Normalização e Codificação).

        Criação de features (Engenharia de atributos).

    Análise Exploratória de Dados (EDA):

        Visualização da distribuição de classes (Balanceamento).

        Correlação entre frequência/notas e a evasão.

        Identificação de padrões em variáveis demográficas.

    Modelagem:

        Algoritmo utilizado: Random Forest Classifier (Florestas Aleatórias).

        Justificativa: Capacidade de lidar com não-linearidade e fornecer a importância das variáveis.

    Avaliação:

        Métricas: Acurácia, Precision, Recall e F1-Score.

        Análise da Matriz de Confusão.

🛠 Tecnologias Utilizadas

    Linguagem: Python 3.x

    Bibliotecas Principais:

        Pandas (Manipulação de dados)

        Numpy (Cálculos numéricos)

        Seaborn & Matplotlib (Visualização de dados)

        Scikit-learn (Machine Learning e Métricas)

📈 Resultados Esperados

O modelo fornece:

    Uma classificação binária para cada aluno (0 = Probabilidade de Ficar, 1 = Risco de Evasão).

    Um ranking das variáveis mais importantes (Feature Importance), permitindo à instituição focar nos fatores críticos (ex: Notas do 1º semestre, Frequência, Distância, etc).
