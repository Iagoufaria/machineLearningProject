from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. PREPARAÇÃO
X = df[['Idade', 'Nota_Semestre_1', 'Frequencia_Perc', 'Bolsista', 'Distancia_Casa_Km']]
y = df['Evasao']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#CRIAÇÃO E TREINAMENTO DO MODELO
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train) # Aprendizado de padrões

#PREVISÃO E AVALIAÇÃO
y_pred = modelo.predict(X_test)

print("--- RESULTADOS DO MODELO ---")
print(f"Acurácia (Porcentagem de Acertos): {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nRelatório Detalhado:")
print(classification_report(y_test, y_pred))

#QUAIS VARIÁVEIS FORAM MAIS IMPORTANTES?
feature_imp = pd.Series(modelo.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nO que mais pesou na decisão da IA?")
print(feature_imp)

#Visualizar a Matriz de Confusão
plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão (Acertos e Erros)')
plt.ylabel('Realidade (0=Ficou, 1=Saiu)')
plt.xlabel('Previsão do Modelo')
plt.show()