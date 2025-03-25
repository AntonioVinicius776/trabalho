import matplotlib.pyplot as plt #importando a biblioteca de visualização grafica

#estilo do grafico
plt.style.use('Solarize_Light2')

#definindo tamanho do grafico
plt.figure(figsize=(10,5))

#lista de dados a serem exibidos
ano=[1,2,3]
carambola=[7,8,10]
fruta_antiga=[4,5,6]

#rotulo do eixo x
plt.xlabel("x")
#rotuko do eixo y
plt.ylabel("y")

#plotando no grafico os dados das listas x e y respectivamente
plt.plot(ano,carambola,label='carambola',linestyle='--',color='r',marker='o')#especificações sobre os detalhes visuais das linhas
plt.plot(ano,fruta_antiga,label='fruta_antiga',marker='o')

#referenciando as linhas do grafico na ordem em que foram plotadas
plt.legend()
#colocando grade no grafico
plt.grid(True)
#executando/mostrando o grafico
plt.show()