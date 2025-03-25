import matplotlib.pyplot as plt#importando uma biblioteca de visualização grafica
import pandas as pd#importando uma biblioteca de manipulação de dados

#lendo o arquivo csv
a=pd.read_csv('g_learn.csv')

#definindo tamanho do grafico
plt.figure(figsize=(10,5))

#rotulo do eixo x
plt.xlabel("x")
#rotuko do eixo y
plt.ylabel("y")

#plotando no grafico os dados das listas x e y respectivamente
plt.plot(a['ano'],a['carambolap'],label='produtividade',linestyle='--',color='r',marker='o')#especificações sobre os detalhes visuais das linhas como tambem
plt.plot(a['ano'],a['carambolac'],label='custo',marker='o')#informando os rotulos especificados as linhas do grafico


#referenciando as linhas do grafico na ordem em que foram plotadas
plt.legend()
#colocando grade no grafico
plt.grid(True)
#executando/mostrando o grafico

plt.ylim([0,10000])

plt.show()