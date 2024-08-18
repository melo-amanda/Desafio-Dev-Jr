import pandas as pd

#Cria um csv para realização de testes
data = [
    {"equipmentId": "EQ-12495", "timestamp": "2023-02-12T01:30:00.000-05:00", "value": 78.8},
    {"equipmentId": "EQ-12492", "timestamp": "2023-01-12T01:30:00.000-05:00", "value": 8.8},
]

df = pd.DataFrame(data)

filename = "leitura_sensor_manual.csv"
df.to_csv(filename, index=False)

print(f"Arquivo '{filename}' criado com sucesso!")