import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# API UV Index - ainda funciona gratuitamente em algumas contas
UV_URL = "https://api.openweathermap.org/data/2.5/uvi"

# Alternativa: API Open-Meteo (gratuita, sem API key)
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def get_uv_index(lat: float, lon: float) -> float | None:
    """
    Busca o índice UV atual
    Tenta primeiro OpenWeather, depois Open-Meteo como fallback
    """

    # Tenta OpenWeather primeiro (se você tiver acesso)
    if API_KEY:
        try:
            params = {
                "lat": lat,
                "lon": lon,
                "appid": API_KEY,
            }
            response = requests.get(UV_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("value")
        except:
            pass  # Se falhar, tenta a próxima opção

    # Fallback: Open-Meteo (gratuita e confiável)
    try:
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "uv_index",
            "timezone": "auto",
        }
        response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["current"]["uv_index"]
    except requests.RequestException:
        return None
    except KeyError:
        return None
