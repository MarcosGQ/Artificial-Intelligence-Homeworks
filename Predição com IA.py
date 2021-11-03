import pandas as pd
import numpy as np

# pre processamento
base= pd.read_csv('credit_data.csv')

# tratamento dos dados invalidos, por idade
# excluindo pessoas menores de 18, pois não podem arcar com a responsabilidade
# do exercicio proposto: pagamento de emprestimo
base.loc[base.age < 18, 'age'] = 40.92
               
# divisao de previsores e classe
previsores= base.iloc[:, 1:4].values
classe= base.iloc[:, 4].values

# uso do imputer para retirar retirar os valores faltantes
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values= np.nan, strategy= 'mean')
imputer= imputer.fit(previsores[:, 1:4])
previsores[:, 1:4]= imputer.transform(previsores[:, 1:4])

# escalonamento dos dados
from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
previsores= scaler.fit_transform(previsores)

# dividindo a base de dados em treinamento e teste
from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste= train_test_split(previsores, classe, test_size= 0.25, random_state= 0)

# importação da biblioteca SVM
from sklearn.svm import SVC

# construção do classificador com kernel rbf com custo de 2.0
classificador= SVC(kernel= 'rbf', random_state= 1, C= 2.0)

# criação do classificador
classificador.fit(previsores_treinamento, classe_treinamento)

# pegar os 500 registros de teste e submete los ao SVM para ver de qual parte 
# da reta eles vao "cair", e gerar a respectiva classificação
previsoes= classificador.predict(previsores_teste)

# calculo de precisao e matriz de confusão
from sklearn.metrics import confusion_matrix, accuracy_score
precisao= accuracy_score(classe_teste, previsoes)
matriz= confusion_matrix(classe_teste, previsoes)
