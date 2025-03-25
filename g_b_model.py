import pandas as pd
import matplotlib.pyplot as plt

# Leia os dados do arquivo CSV
df = pd.read_csv('g_learn.csv')

# Exemplo de gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(df['crops'], df['produtividade'])
plt.title('Gráfico de Barras')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.show()
