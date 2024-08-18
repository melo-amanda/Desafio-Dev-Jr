from flask import Flask, request, jsonify
from BancoMod import update_table, select_data
import csv

app = Flask(__name__)

#Endpoint para receber dados do sensor em formato json
@app.route("/receive-reading", methods=["POST"])
def receive_reading():
    data = request.get_json()

    #Checa a formatação do json
    if 'equipmentId' not in data or 'timestamp' not in data or 'value' not in data:
        return jsonify({"error": "Wrong format"}), 400
    
    #Define as variáveis a serem salvas e chama a função para salvarem os dados no banco de dados
    equipmentId = data['equipmentId']
    timestamp = data['timestamp']
    value = data['value']
    update_table(equipmentId, timestamp, value)

    return jsonify({"success": "Data stored"}), 201

#Endpoint para receber dados manualmente em formato csv
@app.route("/receive-csv", methods=["POST"])

def receive_csv():
    file = request.files['file']
    
    #Checa se o arquivo foi enviado
    if not file:
        return jsonify({"error":"No file selected"}), 400
    
    #Checa se o tipo de arquivo é csv
    if file and file.filename.endswith('.csv'):
        #Tenta a leitura do arquivo csv para armazená-lo eem variáveis e salvá-lo no banco de dados
        try:
            file_content = file.stream.read().decode("utf-8")
            csv_file = csv.DictReader(file_content.splitlines())
            for row in csv_file:
                equipmentId = row["equipmentId"]
                timestamp = row["timestamp"]
                value = row["value"]
                update_table(equipmentId, timestamp, value)
            return jsonify({"success": "CSV data saved"}), 201
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    return jsonify({"error": "Invalid file"}), 400

#Endpoint para resgatar os dados armazenados no banco de dados
@app.route("/get-data")

def get_data():
    data = select_data()
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
