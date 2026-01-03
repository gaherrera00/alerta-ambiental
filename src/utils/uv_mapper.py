def interpretar_uv(uv_index: float | None) -> str:
    if uv_index is None:
        return "N/D"

    if uv_index < 3:
        return "Baixo"
    elif uv_index < 6:
        return "Moderado"
    elif uv_index < 8:
        return "Alto 🟠"
    elif uv_index < 11:
        return "Muito Alto"
    else:
        return "Extremo"
