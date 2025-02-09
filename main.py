from flask import Flask, request, jsonify, render_template
from data_manager import DataManager
from Observers import LoggerObserver, ReportGeneratorObserver

app = Flask(__name__)

# Instanciando o DataManager e adicionando observadores
data_manager = DataManager()
logger_observer = LoggerObserver()
report_observer = ReportGeneratorObserver()
data_manager.add_observer(logger_observer)
data_manager.add_observer(report_observer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config', methods=['GET'])
def config():
    return render_template('config.html')

@app.route('/json-params-atividade', methods=['GET'])
def json_params():
    params = [
        {"name": "cenario", "type": "text/plain"},
        {"name": "riscos_presentes", "type": "text/plain"},
        {"name": "epis_disponiveis", "type": "text/plain"},
        {"name": "feedback_ativado", "type": "boolean"},
        {"name": "numero_de_tentativas", "type": "integer"},
        {"name": "dificuldade", "type": "text/plain"}
    ]
    return jsonify(params)

@app.route('/deploy-atividade', methods=['POST'])
def deploy_atividade():
    data = request.get_json()
    activity_id = data.get("activityID")

    instances = data_manager.load_instances()
    instances.append({"activityID": activity_id, "status": "deployed"})
    data_manager.save_instances(instances)

    return jsonify({"url": f"https://WorkplaceSafety.repl.co/atividade/{activity_id}"})

@app.route('/analytics-atividade', methods=['POST'])
def analytics():
    data = request.get_json()
    activity_id = data.get("activityID")

    analytics_data = data_manager.load_analytics()
    filtered_data = [
        entry for entry in analytics_data if entry.get("activityID") == activity_id
    ]

    return jsonify(filtered_data)

@app.route('/lista-analytics-atividade', methods=['GET'])
def lista_analytics():
    analytics_list = {
        "qualAnalytics": [{"name": "feedback_gerado", "type": "text/plain"}],
        "quantAnalytics": [
            {"name": "acertos", "type": "integer"},
            {"name": "erros", "type": "integer"},
            {"name": "tempo_gasto", "type": "integer"}
        ]
    }
    return jsonify(analytics_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)