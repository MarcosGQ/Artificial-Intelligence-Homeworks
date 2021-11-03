# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# Carregar dados do arquivo .csv para variavel 'base'
base= pd.read_csv('mt_cars.csv') # Usamos a biblioteca 'pandas' para ler esse arquivo
base.shape # 'shape' da forma a esse arquivo, uma vez que seus dados estão numa variavel (array)

# mpeg= consumo, cyl= cilindros, disp= cilindradas, hp
base.head()

# Exclui a coluna 0 (primeira da esquerda para direita)
base= base.drop(['Unnamed: 0'], axis= 1)

# Regressão linear simples - previsão de consumo de acordo com as cilindradas do automovel
# Criação de X e Y: variavel independente e variavel dependente
# Calculo da correlação entre X e Y
x= base.iloc[:,2].values # coluna disp (cilindradas)
y= base.iloc[:,0].values # coluna mpg (consumo)
correlacao= np.corrcoef(x,y)
correlacao

# Mudança do formato de X para o formato de matriz (obrigatorio para as versoes recentes da biblioteca sklearn)
x= x.reshape(-1,1)

# Criação do modelo, treinamento, visualização dos coeficientes e do score do modelo
modelo= LinearRegression()
modelo.fit(x,y)

# Interceptação (aonde os dados encontram o eixo 'y')
modelo.intercept_

# Inclinação (ângulo da reta)
modelo.coef_

# Score R² (coeficiente de determinação, mostra o quanto o modelo consegue explicar os valores obtidos)
modelo.score(x,y)

# Geração de previsões
previsoes= modelo.predict(x)
previsoes

# Criação do modelo usando a biblioteca statsmodel, para obter R² ajustado (coeficiente de determinaçao ajustado)
modelo_ajustado= sm.ols(formula= 'mpg ~ disp', data= base) # Na formula temos a variavel dependente a esquerda e a independente a direita
modelo_experiente= modelo_ajustado.fit() # O metodo 'fit' treina o modelo
print('Regressao linear simples\n')
#print(modelo_experiente.summary())

# Visualização dos resultados com grafico de dispersão
plt.scatter(x,y)
plt.plot(x, previsoes, color= 'red')

# Previsao para apenas um valor
modelo.predict([[200]]) # Se o veiculo tiver 200 cilindradas, quanto consumira?

# Regressao linear multipla
# Criação de novas variaveis x1 e y1 e novo modelo para comparação com o anterior
# 3 variaveis independentes para prever o consumo: cyl, disp e hp
x1= base.iloc[:,1:4].values # [:,1:4]= pega todas as linhas e as colunas de 1 a 3 (nesse 'range' o ultimo valor é ignorado, no caso, o '4')
y1= base.iloc[:,0].values # Passa o consumo para 'y1'
modelo2= LinearRegression()
modelo2.fit(x1,y1)
modelo2.score(x1,y1)

# Criação do modelo ajustado com mais atributos usando statsmodel
modelo_ajustado2= sm.ols(formula= 'mpg ~ cyl + disp + hp', data= base)
modelo_experiente2= modelo_ajustado2.fit()
print('\nRegressao linear multipla\n')
print(modelo_experiente2.summary())









