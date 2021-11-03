# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# Carregar dados do arquivo .csv para variavel 'base'
base= pd.read_csv('semen.csv') # Usamos a biblioteca 'pandas' para ler 
                               # esse arquivo

base.shape # 'shape' da forma a esse arquivo, uma vez que seus dados estão 
           # numa variavel (array)

# Regressao linear multipla
# 4 variaveis independentes: x1, x2, x3 e x4
x= base.iloc[:,0:4].values # [:,1:4]= pega todas as linhas e as colunas de 
                           # 0 a 3 (nesse 'range' o ultimo valor é ignorado, 
                           # no caso, o '4')
y= base.iloc[:,4].values # Passa a coluna 'y' para a y

# Criação do modelo, treinamento, visualização dos coeficientes e do score
modelo= LinearRegression()
modelo.fit(x,y)

# Interceptação (aonde os dados encontram o eixo 'y')
print('\nInterceptação (aonde os dados encontram o eixo Y)\n')
print(modelo.intercept_)

# Inclinação (ângulo da reta)
print('\nInclinação (ângulo da reta)\n')
print(modelo.coef_)

# Score R² (coeficiente de determinação, mostra o quanto o modelo consegue 
# explicar os valores obtidos)
modelo.score(x,y)

# Geração de previsões
previsoes= modelo.predict(x)
print('\nGerando previsões:\n',previsoes)

# Criação do modelo usando a biblioteca statsmodel, para obter R² ajustado 
modelo_ajustado= sm.ols(formula= 'y ~ x1 + x2 + x3 + x4', data= base)
modelo_experiente= modelo_ajustado.fit() # O metodo 'fit' treina o modelo
print('\nRegressao linear multipla\n')
print(modelo_experiente.summary())

# Visualização dos resultados com grafico de dispersão
# As linhas abaixo estão marcadas como comentário porque não fui capaz de
# desenvolver o gráfico de dispersão para regressão linear multipla
# Erro: "ValueError: x and y must be the same size"
# plt.scatter(x,y)
# plt.plot(x, previsoes, color= 'red')