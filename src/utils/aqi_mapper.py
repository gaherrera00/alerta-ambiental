def interpretar_aqi(aqi: int) -> str:
    """
    Converte o índice AQI (1-5) em descrição legível
    1 = Boa
    2 = Razoável
    3 = Moderada
    4 = Ruim
    5 = Muito ruim
    """
    return {
        1: "Boa",
        2: "Razoável",
        3: "Moderada",
        4: "Ruim",
        5: "Muito ruim",
    }.get(aqi, "Desconhecida")
