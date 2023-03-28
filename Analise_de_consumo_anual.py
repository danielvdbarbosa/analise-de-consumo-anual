#importando bibliotecas
from matplotlib import pyplot as plt
import numpy as np
import random

#inicializando constantes e listas vazias
LISTA_MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
               "Junho", "Julho", "Agosto", "Setembro", "Outubro",
               "Novembro", "Dezembro"]

lista_valores = []
lista_media = []

#populando uma lista de consumos com valores mensais aleatorios entre 100 e 350
for indice, mes in enumerate(LISTA_MESES):
    
    lista_valores.append(random.randint(100,350))
    if indice == 0:
        lista_media.append(lista_valores[indice])
        
    else:
        lista_media.append((lista_valores[indice] + lista_valores[indice-1] ) / 2) 
        
#imprimindo valores das listas
print("\nLista de medias: ", lista_media)
print("\nLista de valores: ", lista_valores)

#realizando comparativo entre dois meses escolhidos
primeiro_mes = int(input("\nDigite o primeiro mês a ser comparado: (Digite de 1 a 12)"))-1
segundo_mes = int(input("\nDigite o segundo mês a ser comparado: (Digite de 1 a 12)"))-1
economia = lista_valores[primeiro_mes] - lista_valores[segundo_mes]
  
if economia > 0: 
    print("\nComparando os meses " + LISTA_MESES[primeiro_mes] + " e " + LISTA_MESES[segundo_mes] +
          " você economizou " + str(economia) + " reais.")

elif economia == 0:
    print("\nO consumo nos dois meses foi igual.")

else:
    print("\nComparando os meses " + LISTA_MESES[primeiro_mes] + " e " + LISTA_MESES[segundo_mes] +
          " você gastou " +  str(abs(economia)) + " reais a mais.")

#abreviando meses para exibição de label no gráfico
meses_abreviados = []
for mes in LISTA_MESES:
    
    meses_abreviados.append(mes[0:3])
print("\nMeses abreviados: ", meses_abreviados)

#calculando estatisticas dos resultados
valor_maximo = np.max(lista_valores)
valor_minimo = np.min(lista_valores)
lista_max = []
lista_min = []
  
for indice, valor in enumerate(lista_valores):
    if valor == valor_maximo:
        
        lista_max.append(LISTA_MESES[indice])
        
    elif valor == valor_minimo:
        
        lista_min.append(LISTA_MESES[indice])

#imprimindo resultados
print("Os meses com maior consumo foram: " + ", ".join(lista_max) + ".")
print("Os meses com menor consumo foram: " + ", ".join(lista_min) + ".")
print("A media de consumo anual foi de " + str(np.average(lista_valores)) + ".")
print("A mediana de consumo anual foi de " + str(np.median(lista_valores)) + ".")

#transferindo as estatisticas para visualizacao grafica
plt.plot(meses_abreviados, lista_valores, label = "Consumo")
plt.plot(meses_abreviados, lista_media, label = "Tendencia")
plt.legend()
plt.show()
plt.clf()