from flask import Flask, render_template, request, jsonify
import requests
import time
from datetime import datetime

app = Flask(__name__)

# Sua chave de API do OpenWeatherMap
API_KEY = '089de9028290ec6f829240e0133046fe'

# Função para obter o clima atual de uma cidade
def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url)
    return response.json()

# Função para obter a previsão de 5 dias de uma cidade
def get_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url)
    return response.json()

# Função para obter a qualidade do ar de uma localização (usando coordenadas)
def get_air_quality(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

# Página inicial que exibe as informações climáticas
@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    forecast = None
    air_quality = None

    if request.method == 'POST':
        city = request.form['city']

        # Clima atual
        weather = get_current_weather(city)

        # Previsão de 5 dias
        forecast = get_forecast(city)

        # Coordenadas para a qualidade do ar
        if weather:
            lat = weather['coord']['lat']
            lon = weather['coord']['lon']
            air_quality = get_air_quality(lat, lon)

    return render_template('index.html', weather=weather, forecast=forecast, air_quality=air_quality)
    
    return daily_data

if __name__ == '__main__':
    app.run(debug=True)
