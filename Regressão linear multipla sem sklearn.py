import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

# Carregar dados do arquivo .csv para variavel 'base'
base= pd.read_csv('semen.csv') # Usamos a biblioteca 'pandas' para ler 
                               # esse arquivo

base.shape # 'shape' da forma a esse arquivo, uma vez que seus dados estão 
           # numa variavel (array)

# Regressao linear multipla
# 4 variaveis independentes: x1, x2, x3 e x4
x1= base.iloc[:,0].values # passa a coluna 0 para x1
x2= base.iloc[:,1].values
x3= base.iloc[:,2].values
x4= base.iloc[:,3].values
y= base.iloc[:,4].values # passa a coluna y para variavel y
# n= uma variável categórica binária
# p= erro comumente distribuído para servir de banco de dados para regressão
# size= tamanho do 'array' de dados de cada variavel
categoria= sp.random.binomial(n=1, p=.5, size=13)
erro= sp.random.normal(size=13)

# organizando os dados em cada variavel e printando para verificar
org= {"y":y, "x1":x1, "x2":x2, "x3":x3, "x4":x4, "categoria":categoria}
dados= pd.DataFrame(data= org)
print("\nDataFrame dos dados:\n", dados)   

# Estatisticas descritivas e distribuição da variavel resposta
print("\nEstatísticas descritivas de y:")
print(dados['y'].describe())

# estimar o modelo e mostrar os resultados
modelo= sm.ols(formula='y~x1+x2+x3+x4+categoria', data=dados).fit()
print(modelo.summary())

# calculo de resíduos (epsilon = y - ŷ)
y_hat= modelo.predict()
residuo= y - y_hat
      
# calcular SQE= somatório de (y - ŷ)²
soma_y= sum(y)
soma_y_hat= sum(y_hat)
SQE= (soma_y - soma_y_hat)**2
print("\nSoma dos quadrados do erro: ", SQE)

# calcular SQT= somatorio de (y - média amostral de ŷ)²
# fazer a média amostral de ŷ
soma_y_hat= soma_y_hat/13
    
SQT= (soma_y - soma_y_hat)**2    
print("\nSoma dos quadrados totais: ", SQT)

# calcular SQR= SQT - SQE
print("\nSoma dos quadrados da regressão: ", SQT-SQE)

# gráfico de residuos
print("\nGráfico de residuos:\n")
plt.scatter(y= residuo, x= y_hat, color= 'blue', s= 50, alpha=.6)
plt.hlines(y= 0, xmin= -10, xmax= 15, color= 'red')
plt.ylabel('$\epsilon = y - \hat{y}$ - Resíduos')
plt.xlabel('$\hat{y}$ ou $E(y)$ - Predito')
plt.show()

# obter os coeficientes da regressão
# reta de regressão entre 'y' e 'x1'
coeficientes = pd.DataFrame(modelo.params)
coeficientes.columns = ['Coeficientes de regressão']
print(coeficientes)

# gráfico de regressão
plt.scatter(x1,y)
plt.title('Reta de regressão')
plt.ylabel('$y$ - Variável Dependente')
plt.xlabel('$x1$ - Preditor')
plt.plot(x1, y, color= 'red')