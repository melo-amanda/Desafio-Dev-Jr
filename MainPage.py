import streamlit as st
import requests
import pandas as pd
import ast
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

st.write("## Análise de Informações dos Sensores")

st.write("### Input Manual")
csv_file = st.file_uploader("Insira o arquivo .csv com os dados complementares:")

#Realiza a chamada da API caso o usuário tenha inserido um arquivo
if csv_file:
    url = "http://127.0.0.1:5000/receive-csv"
    filekey = {"file": csv_file}
    post_request = requests.post(url,files= filekey)
    st.write(post_request.text)

##################################################################################

#Métodos e Funções
#Requisição dos dados salvos no banco de dados
url = "http://127.0.0.1:5000/get-data"
get_request = requests.get(url)

dict_array = ast.literal_eval(get_request.text)
#Retira a coluna id
df = pd.DataFrame(dict_array).drop(columns=["id"])
#Transforma a coluna timestamp em tipo datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
#Retira o Fuso Horário
df['timestamp'] = df['timestamp'].dt.tz_localize(None)
#Retira o índice
df.reset_index(drop=True, inplace=True)

#Função para filtrar o data frame de acordo com o período selecionado
def filter_data(days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]
#Calcula a média do data frame filtrado
def period_mean(period_df):
    return period_df.groupby('equipmentId').mean()

###################################################################################

#Interface
st.write("### Gráficos")
#Cria duas colunas de informação
info_col1,info_col2 = st.columns(2)

#Seleciona o período para analisar as informações
time_range = info_col1.selectbox("Selecione o intervalo de tempo:", 
                          ["Últimas 24 horas", "Últimas 48 horas", "Última semana", "Último mês"])
if time_range == "Últimas 24 horas":
    days = 1
elif time_range == "Últimas 48 horas":
    days = 2
elif time_range == "Última semana":
    days = 7
else:
    days = 30

#Apresenta a média das leituras
filtered_df = filter_data(days=days)
info_col2.write("Média dos valores dos sensores para o intervalo:")
info_col2.write(period_mean(filtered_df).drop(columns=["timestamp"]))

#Gráfico para visualizar as leituras individuais dentro do período selecionado
fig, ax = plt.subplots()
equipmentIds = df["equipmentId"].unique()

for id in equipmentIds:
    data = filtered_df[filtered_df['equipmentId'] == id]
    ax.plot(data['timestamp'], data['value'], marker='o', label=id)

#Formatação do gráfico
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
ax.set_xlabel('Timestamp')
ax.set_ylabel('Value')
ax.legend(title='Equipment ID')
ax.grid(True)

st.pyplot(fig)

