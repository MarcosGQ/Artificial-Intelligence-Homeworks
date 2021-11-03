# Iniciando os valores dos pesos, taxa de aprendizado e degrau
# 'degrau' é a variavel para verificar se o neuronio vai ou nao ativar 
peso1= -0.2 # valor aleatorio inicial
peso2= 0.4
tax_aprendizado= 0.2 # o qual rapido quer que o algoritmo aprenda (entre 0 a 1)
degrau= 0 # igual a 0 por padrão, para a porta logica OR
           # se fosse AND, degrau deveria ser igual a 1

# base de dados de treinamento dos possiveis resultados da porta logica OR
treino= [0,1,1,1]

# função Step Function
def stepFunction(num):
    if(num>degrau):
        num= 1 # peso positivo, sinapse excitadora
    elif(num<=degrau):
        num= 0 # peso negativo, sinapse inibidora
    return num

# função de calculo de erro, algoritmo mais simples:
# erro = respostaCorreta - respostaCalculada    
def erroCalc(treino, respCalc):
    erro= treino - respCalc
    return erro

# função de atualização dos pesos
# peso(n+1)= peso(n) + (taxa de aprendizado * entrada * erro)
def atualizaPeso(pesoN, entrada, erro):
    pesoN1= pesoN +(tax_aprendizado * entrada * erro)
    return pesoN1

# rodando os treinamentos, epoch= 10 (10 treinamentos)
for epoch in range (10):
    print("\nEPOCH Nº {}".format(epoch+1))
    it= 0
    # cada treino testa as 4 possibilidades de entradas da porta logica OR
    
    for entrada1 in range(2): # atribui valores 0 e 1 para entrada1
        for entrada2 in range(2): # atribui valores 0 e 1 para entrada2
            print("\nEntrada 1 = {} , Entrada 2 = {}".format(entrada1,entrada2))
            print("Peso 1 = {} ,  Peso 2 = {}".format(peso1,peso2))
            
            # faz somatorio das entradas * pesos
            soma = (peso1*entrada1)+(peso2*entrada2)
            # chama stepFunction para verificar essa sinapse
            soma = stepFunction(soma)
            
            # stepFunction converte para 1 quaisquer valores maiores que 0
            # e para 0, quaisquer valores menores ou iguais a esse.
            # O valor retornado por stepFunction é a resposta do algoritmo
            # para as entradas 1 e 2 da porta lógica OR
            print("Valor de saída atual = {}".format(soma))
            
            # imprime o valor correto (valor almejado como resultado)
            print("Valor de saída esperado = {}".format(treino[it]))
            
            # calcula o erro
            Erro = erroCalc(treino[it], soma)
            print("Erro = {}".format(Erro))
            
            # Erro = 0 significa que o algoritmo não errou
            # Se errou, chama a função para atualizar os pesos
            if(Erro!=0):
                peso1= atualizaPeso(peso1,entrada1,Erro)
                print("Peso 1 atualizado = {}".format(peso1))
                peso2= atualizaPeso(peso2,entrada2,Erro)
                print("Peso 2 atualizado = {}".format(peso2))
            it+= 1