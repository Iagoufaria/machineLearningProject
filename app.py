import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. CRIAÇÃO DE DADOS FICTÍCIOS (Simulando seu Dataset) ---
# Na prática, você substituiria isso por: df = pd.read_csv('seus_dados.csv')
np.random.seed(42) # Para garantir que os resultados sejam iguais sempre que rodar
n_alunos = 200

data = {
    'Idade': np.random.randint(18, 35, n_alunos),
    'Nota_Semestre_1': np.random.uniform(0, 10, n_alunos).round(1),
    'Frequencia_Perc': np.random.uniform(50, 100, n_alunos).round(1),
    'Bolsista': np.random.choice([0, 1], n_alunos, p=[0.7, 0.3]), # 0=Não, 1=Sim
    'Distancia_Casa_Km': np.random.uniform(1, 50, n_alunos).round(1)
}

df = pd.DataFrame(data)

# Criando a variável alvo 'Evasao' (0 = Ficou, 1 = Saiu) baseada em regras para o modelo ter o que aprender
# Lógica: Quem tem nota baixa E frequência baixa tem mais chance de sair
def definir_evasao(row):
    score = row['Nota_Semestre_1'] * 0.6 + (row['Frequencia_Perc']/10) * 0.4
    if score < 6.5:
        return np.random.choice([0, 1], p=[0.2, 0.8]) # Alta chance de evasão
    else:
        return np.random.choice([0, 1], p=[0.9, 0.1]) # Baixa chance de evasão

df['Evasao'] = df.apply(definir_evasao, axis=1)

# --- 2. ANÁLISE EXPLORATÓRIA (VISUALIZAÇÕES) ---

# Configuração de estilo
sns.set_style("whitegrid")
plt.figure(figsize=(15, 5))

# GRÁFICO 1: Distribuição da Variável Alvo (Balanceamento)
plt.subplot(1, 3, 1)
ax = sns.countplot(x='Evasao', data=df, palette='coolwarm')
plt.title('Contagem de Alunos: Ficaram (0) vs Evadiram (1)')
plt.xlabel('Situação')
plt.ylabel('Quantidade')

# GRÁFICO 2: Boxplot - Relação entre Notas e Evasão
plt.subplot(1, 3, 2)
sns.boxplot(x='Evasao', y='Nota_Semestre_1', data=df, palette='Set2')
plt.title('Distribuição de Notas por Grupo')
# Se a caixa laranja (1) estiver mais baixa, confirma que notas baixas influenciam a evasão.

# GRÁFICO 3: Correlação (Mapa de Calor)
plt.subplot(1, 3, 3)
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='RdBu', fmt=".2f", vmin=-1, vmax=1)
plt.title('Matriz de Correlação')

plt.tight_layout()
plt.show()

# --- 3. ESTATÍSTICAS DESCRITIVAS ---
print("Médias agrupadas por Evasão:")
print(df.groupby('Evasao')[['Nota_Semestre_1', 'Frequencia_Perc', 'Idade']].mean())