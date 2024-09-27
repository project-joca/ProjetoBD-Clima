from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Sua chave de API do OpenWeatherMap
API_KEY = '089de9028290ec6f829240e0133046fe'

# Função para obter os dados climáticos
def obter_dados_climaticos(cidade):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/previsao', methods=['POST'])
def previsao():
    cidade = request.form['cidade']
    dados = obter_dados_climaticos(cidade)
    
    if dados:
        clima = {
            'cidade': cidade,
            'temperatura': dados['main']['temp'],
            'descricao': dados['weather'][0]['description'],
            'umidade': dados['main']['humidity'],
            'vento': dados['wind']['speed']
        }
        return render_template('previsao.html', clima=clima)
    else:
        erro = "Não foi possível obter os dados climáticos. Verifique o nome da cidade."
        return render_template('index.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
