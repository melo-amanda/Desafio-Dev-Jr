# Desafio Desenvolvedora Jr - Análise de Dados de Sensores

## Descrição

Este projeto foi desenvolvido como solução do desafio técnico de um processo seletivo. O objetivo do desafio é desenvolver uma API para receber, armazenar e acessar dados de sensores, recebidos no formato json ou csv. Além disso, a solução inclui uma interface para o input manual do documento csv e análise das informações dos sensores em diferentes intervalos de tempo (24 horas, 48 horas, 1 semana, 1 mês).

## Estrutura

- **BancoMod.py**: Spript responsável pela criação da tabela `leitura_sensor`, presente no arquivo **BancoDesafio**, inserção e acesso aos dados da tabela.
- **APIConstruct.py**: Construção da API para recepção de dados de sensores via POST requests e requisição dos dados armazenados via GET request.
- **GerarCSV.py**: Script para gerar um arquivo CSV a partir dos dados exemplificados no desafio para realização de testes.
- **MainPage.py**: Interface do usuário usando Streamlit para visualização dos dados dos sensores e input de arquivos.
- **leitura_sensor_manual.csv**: Arquivo CSV exemplo utilizado para demonstrar a inserção manual de dados.

### Requisitos

- Python 3
- Bibliotecas: `pandas`, `sqlite3`, `streamlit`, `csv`, `requests`, `ast`, `matplotlib`, `datetime`

