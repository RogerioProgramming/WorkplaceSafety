from flask import Flask, request, jsonify, render_template
import os
import json

app = Flask(__name__)

# Classe Singleton para gerenciar dados
class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.data_folder = "data"
        self.instances_file = os.path.join(self.data_folder, "instances.json")
        self.analytics_file = os.path.join(self.data_folder, "analytics.json")
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        os.makedirs(self.data_folder, exist_ok=True)
        if not os.path.exists(self.instances_file):
            with open(self.instances_file, "w") as f:
                json.dump([], f)  # Inicia com uma lista vazia
        if not os.path.exists(self.analytics_file):
            with open(self.analytics_file, "w") as f:
                json.dump([], f)  # Inicia com uma lista vazia

    def load_instances(self):
        with open(self.instances_file, "r") as f:
            return json.load(f)

    def save_instances(self, instances):
        with open(self.instances_file, "w") as f:
            json.dump(instances, f, indent=4)

    def load_analytics(self):
        with open(self.analytics_file, "r") as f:
            return json.load(f)

    def save_analytics(self, analytics):
        with open(self.analytics_file, "w") as f:
            json.dump(analytics, f, indent=4)


# Instancia o gerenciador de dados (Singleton)
data_manager = DataManager()


# Página inicial
@app.route('/')
def index():
    return render_template('index.html')


# Página de configuração da atividade
@app.route('/config', methods=['GET'])
def config():
    return render_template('config.html')


# Serviço para retornar parâmetros da configuração
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


# Deploy da atividade
@app.route('/deploy-atividade', methods=['POST'])
def deploy_atividade():
    data = request.get_json()
    activity_id = data.get("activityID")

    # Lógica para salvar a atividade no arquivo instances.json
    instances = data_manager.load_instances()
    instances.append({"activityID": activity_id, "status": "deployed"})
    data_manager.save_instances(instances)

    return jsonify({"url": f"https://WorkplaceSafety.repl.co/atividade/{activity_id}"})


# Serviço para obter analytics
@app.route('/analytics-atividade', methods=['POST'])
def analytics():
    data = request.get_json()
    activity_id = data.get("activityID")

    # Carrega os dados de analytics e filtra pela atividade
    analytics_data = data_manager.load_analytics()
    filtered_data = [
        entry for entry in analytics_data if entry.get("activityID") == activity_id
    ]

    return jsonify(filtered_data)


# Serviço para listar analytics
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