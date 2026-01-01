import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/air_pollution"


def qualidade_ar(lat: float, lon: float) -> dict:
    if not API_KEY:
        raise RuntimeError("API KEY não encontrada")

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        info = data["list"][0]

        return {
            "aqi": info["main"]["aqi"],
            "pm2_5": info["components"]["pm2_5"],
            "pm10": info["components"]["pm10"],
            "co": info["components"]["co"],
            "no2": info["components"]["no2"],
            "o3": info["components"]["o3"],
        }

    except requests.RequestException as e:
        raise RuntimeError("Erro ao buscar qualidade do ar") from e
