import pandas as pd
import matplotlib.pyplot as plt

# Leia os dados do arquivo CSV
df = pd.read_csv('glearn.csv')

# Exemplo de gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(df['crops'], df['produtividade'], marker='o')
plt.title('Gráfico de Linha')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.grid(True)
plt.show()

# Exemplo de gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(df['crops'], df['produtividade'])
plt.title('Gráfico de Barras')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.show()

# Exemplo de gráfico de dispersão
plt.figure(figsize=(10, 5))
plt.scatter(df['crops'], df['produtividade'])
plt.title('Gráfico de Dispersão')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.show()