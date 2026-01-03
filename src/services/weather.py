import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def tempo(cidade: str) -> dict:
    if not API_KEY:
        raise RuntimeError("API KEY não encontrada")

    params = {"q": cidade, "appid": API_KEY, "units": "metric", "lang": "pt_br"}

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        resultado = {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "sensacao_termica": data["main"]["feels_like"],
            "umidade": data["main"]["humidity"],
            "vento_kmh": round(data["wind"]["speed"] * 3.6, 1),
            "visibilidade_m": data["visibility"],
            "descricao_tempo": data["weather"][0]["description"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"],
        }

        return resultado

    except requests.RequestException as e:
        raise RuntimeError("Erro ao buscar dados do clima") from e
