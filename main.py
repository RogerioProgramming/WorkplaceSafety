from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

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
    # Lógica para criar e preparar a atividade
    return jsonify({"url": f"https://WorkplaceSafety.repl.co/atividade/{activity_id}"})

# Serviço para obter analytics
@app.route('/analytics-atividade', methods=['POST'])
def analytics():
    data = request.get_json()
    activity_id = data.get("activityID")
    # Exemplo de retorno de analytics
    analytics_data = [
        {
            "inveniraStdID": "1001",
            "quantAnalytics": [{"name": "acertos", "value": 5}, {"name": "tempo_gasto", "value": 300}],
            "qualAnalytics": [{"name": "feedback", "value": "Ótima interação!"}]
        }
    ]
    return jsonify(analytics_data)

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