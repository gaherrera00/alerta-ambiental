import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
ONECALL_URL = "https://api.openweathermap.org/data/3.0/onecall"


def get_uv_index(lat: float, lon: float) -> float | None:
    """
    Busca o índice UV atual usando a API OneCall 3.0
    Retorna None se houver erro (API pode requerer assinatura paga)
    """
    if not API_KEY:
        raise RuntimeError("API KEY não encontrada")

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "exclude": "minutely,hourly,daily,alerts",
    }

    try:
        response = requests.get(ONECALL_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data["current"]["uvi"]

    except requests.RequestException:
        # Se a API falhar (ex: requer assinatura), retorna None
        return None
    except KeyError:
        # Se a estrutura da resposta não tiver o campo esperado
        return None
