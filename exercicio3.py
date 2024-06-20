# -*- coding: utf-8 -*-
"""exercicio3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/121L7yAmFRKtHXGA7GcoVi55nVUqiMl9-
"""

import numpy as np



def xfunction (Cont):
    Lambda= 200 # Taxa de chegada dos pacotes
    mu =256000/(128*8) # Taxa de servico
    elemento_Fila = 0 # quantidade de pacotes na fila inicialmente
    elemento_servidor = 1 # quantidade de pacotes no servico
    K=0  # Primeira iteracao
    t=0  # Tempo inicial
    tc=t+np.random.exponential((1/Lambda)) # Tempo de chegada
    tp=t+np.random.exponential((1/mu)) # Tempo de partida
    t=min(tc,tp)
    Tempo_chegada =[0]     # Armazena os tempos de chegadas dos pacotes
    Tempo_partida =[]      # Armazena os tempos de partidas dos pacotes
    Tq=[]     # tempo no medio que um pacote passa na fila
    #Cont=5    #Tamanho do buffer
    Block=0    # Contador de bloqueio
    n=0         #Numero de pacote que chegam
    while K<110000:
        if tc<tp:  # chegada de um novo pacote
            n=n+1
            tc=t+np.random.exponential((1/Lambda))  #Gera um novo tempo de chegada e suma com t
            if elemento_servidor==1: # Se o servidor estc ocupado
                if elemento_Fila==Cont:
                    Block=Block+1
                elif elemento_Fila<Cont:
                    Tempo_chegada=np.append(Tempo_chegada,t) # Armazena o tempo de chegada
                    elemento_Fila=elemento_Fila+1  # coloco o pacote na fila
            elif elemento_servidor==0: # Se o servidor esta desocupado?
                elemento_servidor=1  # Ocupo o servidor
                Tempo_chegada=np.append(Tempo_chegada,t) #Armazena o tempo de chegada
                tp=t+np.random.exponential((1/mu)) # Gera novo tempo de partida

        elif tc>tp: #  partida de um novo pacote
            K=K+1
            Tempo_partida = np.append(Tempo_partida, t) #armazena o tempo da partida
            Tq = np.append(Tq, (Tempo_partida[K-1]-Tempo_chegada[K-1])) # calcula o tempo no sistema
            if elemento_Fila>0:
                elemento_Fila=elemento_Fila-1    # Decrementa um  pacote da fila
                tp=t+np.random.exponential((1/mu)) # Gera um novo tempo de partida
                elemento_servidor=1  # Ocupa o servidor
            elif elemento_Fila==0: # Se a fila esta vazia
                elemento_servidor=0 # Libera o servidor
                tp=np.infty # Tempo de partida e infinito
        t=min(tc,tp) # Atualiza o tempo para o proximo evento
    Pb=Block/n
    Etq =(np.mean(Tq))
    Eq=Lambda*Etq*(1-Pb)
    out=[Pb,Etq,Eq]
    return out

Saida1=xfunction(1)
Saida2=xfunction(5)
Saida3=xfunction(10)
Saida4=xfunction(15)

print(Saida1)



print("A probabilidade de bloqueio para um tamanho de buffer = 1 é : ", Saida1[0] )
print("O número médio de elementos para um tamanho de buffer = 1 é: ", Saida1[2] )
print("O tempo médio no sistema para um tamanho de buffer = 1 é : ", Saida1[1])

print("A probabilidade de bloqueio para um tamanho de buffer = 5 é: ", Saida2[0] )
print("O número médio de elementos para um tamanho de buffer = 5 é: ", Saida2[2])
print("O tempo médio no sistema para um tamanho de buffer = 5 é : ", Saida2[1])

print("A probabilidade de bloqueio para um tamanho de buffer = 10 é: ", Saida3[0] )
print("O número médio de elementos para um tamanho de buffer = 10 é: ", Saida3[2])
print("O tempo médio no sistema para um tamanho de buffer = 10   é: ", Saida3[1])


print("A probabilidade de bloqueio para um tamanho de buffer = 15 é: ", Saida4[0] )
print("O número médio de elementos para um tamanho de buffer = 15 é: ", Saida4[2])
print("O tempo médio no sistema para um tamanho de buffer = 15   é: ", Saida4[1])