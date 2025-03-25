import matplotlib.pyplot as plt #importando a biblioteca de visualização grafica

#estilo do grafico
plt.style.use('Solarize_Light2')

#definindo tamanho do grafico
plt.figure(figsize=(10,5))

#lista de dados a serem exibidos
x=[1,2,3]
max=[7,8,10]
min=[4,5,6]

#rotulo do eixo x
plt.xlabel("x")
#rotulo do eixo y
plt.ylabel("y")

#plotando no grafico os dados das listas x e y respectivamente
plt.plot(x,max,label='mais',linestyle='--',color='r',marker='o')#especificações sobre os detalhes visuais das linhas como tambem
plt.plot(x,min,label='menos',marker='o')#informando os rotulos especificados as linhas do grafico

#aplicando os rotulos as linhas do grafico como dito na variavel "label" e especificando a localização
plt.legend(loc='upper right')
#colocando grade no grafico
plt.grid(True)
#executando/mostrando o grafico
plt.show()