"""
Módulo de cálculo de riscos baseado em métricas climáticas
"""


def risco_calor(feels_like: float) -> str:
    """Calcula risco baseado na sensação térmica"""
    if feels_like >= 35:
        return "ALTO"
    elif feels_like >= 30:
        return "MÉDIO"
    return "BAIXO"


def risco_calor_umido(feels_like: float, umidade: int) -> str:
    """Calcula risco de calor com umidade alta"""
    if feels_like >= 30 and umidade >= 70:
        return "ALTO"
    elif feels_like >= 28 and umidade >= 60:
        return "MÉDIO"
    return "BAIXO"


def risco_calor_seco(feels_like: float, umidade: int) -> str:
    """Calcula risco de calor seco"""
    if feels_like >= 32 and umidade < 30:
        return "ALTO"
    elif feels_like >= 28 and umidade < 40:
        return "MÉDIO"
    return "BAIXO"


def risco_frio(temp: float, chuva: bool = False) -> str:
    """Calcula risco do frio"""
    if temp <= 10 and chuva:
        return "ALTO"
    elif temp <= 12:
        return "MÉDIO"
    return "BAIXO"


def risco_tempo_seco(umidade: int) -> str:
    """Calcula risco do ar seco"""
    if umidade < 30:
        return "ALTO"
    elif umidade < 40:
        return "MÉDIO"
    return "BAIXO"


def risco_vento(vento_kmh: float) -> str:
    """Calcula risco do vento"""
    if vento_kmh >= 40:
        return "ALTO"
    elif vento_kmh >= 25:
        return "MÉDIO"
    return "BAIXO"


def risco_poluicao(aqi: int, pm2_5: float) -> str:
    """Calcula risco da poluição do ar"""
    if aqi >= 4 or pm2_5 >= 35:
        return "ALTO"
    elif aqi == 3 or pm2_5 >= 25:
        return "MÉDIO"
    return "BAIXO"


def risco_uv(uv_index: float) -> str:
    """
    Calcula risco de exposição UV
    0-2: Baixo
    3-5: Moderado
    6-7: Alto
    8-10: Muito Alto
    11+: Extremo
    """
    if uv_index >= 8:
        return "ALTO"
    elif uv_index >= 6:
        return "MÉDIO"
    return "BAIXO"


def risco_instabilidade(temp_atual: float, temp_anterior: float) -> str:
    """Calcula risco de mudança brusca de temperatura"""
    variacao = abs(temp_atual - temp_anterior)
    if variacao >= 8:
        return "ALTO"
    elif variacao >= 5:
        return "MÉDIO"
    return "BAIXO"


def risco_geral(riscos: list[str]) -> str:
    """Calcula o risco geral baseado em múltiplos riscos"""
    if "ALTO" in riscos:
        return "ALTO"
    elif "MÉDIO" in riscos:
        return "MÉDIO"
    return "BAIXO"
