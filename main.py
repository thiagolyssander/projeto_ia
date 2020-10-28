import numpy as np

# REDE NEURAL MULTICAMADA
# IMPLEMENTAÇÃO DA REDE NEURAL PARA EXEMPLIFICAR O FUNCIONAMENTO NO ARTIGO
# NESTA REDE NEURAL É CALCULADO PARA O RECONHECIMENTO DA PORTA XOR

#FUNÇÃO DE SIGMOID
def sigmoid(soma):
    return 1/(1 + np.exp(-soma))

linha = 4
coluna = 3

# Entradas
Entrada = [[0,0],
           [0,1],
           [1,0],
           [1,1]]
# Resultado esperado
Saida = [[0],
        [1],
        [1],
        [0]]

# Pesos da camada de entrada para a camada de saida
pesos_entrada = [[-0.424,-0.740,-0.961],
                [0.358,-0.577,-0.469]]

# Pesos da camada oculta
pesos_saida = [[-0.017],[-0.893],[0.148]]

# Criação das matrizes para armazenamento de resultados.
hidden2 = np.zeros((linha,coluna))
hidden3 = np.zeros((linha,1))
resultadoFinal = np.zeros((linha,1))
erro = np.zeros((linha,1))

# Calculo das entradas pelos pesos.
for i in range(linha):
    for j in range(coluna):
        somaSinapse = Entrada[i][0] * pesos_entrada[0][j] + Entrada[i][1] * pesos_entrada[1][j]
        hidden2[i][j] = (sigmoid(somaSinapse))


# Calcula validação com pesos finais
for i in range(linha):
    for j in range(coluna):
        hidden3[i][0] += hidden2[i][j] * pesos_saida[j][0]   
    
# Calculo da saida    
for i in range(linha):
    resultadoFinal[i][0] = sigmoid(hidden3[i][0])


# Calculo do erro
for i in range(linha):
    erro[i][0] = Saida[i][0] - resultadoFinal[i][0]


print('### Resultados da Soma das Sinapses pelo pesos ###')
print(hidden2)
print('')
print('### Resultados da Soma das Sinapses pelo pesos e calculado com os pesos finais ###')
print(hidden3)
print('')
print('### Resultado final calculado ###')
print(resultadoFinal)
print('')
print('### Calculo do erro ###')
print(erro)
