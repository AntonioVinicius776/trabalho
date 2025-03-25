#Gráfico 1: Relação entre IDH e Taxa de Fecundidade → 
# Mostra que países com maior IDH tendem a ter uma taxa de fecundidade menor.

#importando uma biblioteca de visualização grafica
import matplotlib.pyplot as plt
#importando uma biblioteca de manipulação de dados
import pandas as pd

tf=pd.read_csv('dados.csv',delimiter=';')
plt.figure(figsize=(10,5))

plt.plot(tf['ano'],tf['fertilidademb'])
#plt.plot(tf['ano'],tf['fertilidademlb'])
#plt.plot(tf['ano'],tf['fertilidademfp'])
#plt.plot(tf['ano'],tf['fertilidademus'])
#plt.plot(tf['ano'],tf['fertilidademm'])

plt.xlim(1999,2025)
#plt.ylim(0,5)

#plt.grid(True)
plt.legend()
plt.show()