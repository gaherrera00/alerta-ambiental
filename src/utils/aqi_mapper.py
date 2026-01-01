def interpretar_aqi(aqi: int) -> str:
    return {
        1: "Boa 🟢",
        2: "Razoável 🟡",
        3: "Moderada 🟠",
        4: "Ruim 🔴",
        5: "Muito ruim 🟣",
    }.get(aqi, "Desconhecida")
