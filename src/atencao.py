def atencao_calor(risco: str) -> str:
    """Riscos de saúde relacionados ao calor"""
    if risco == "ALTO":
        return "Desidratação, insolação, queda de pressão, exaustão térmica"
    elif risco == "MÉDIO":
        return "Desidratação, fadiga, mal-estar"
    else:
        return ""


def atencao_calor_umido(risco: str) -> str:
    """Riscos de saúde com calor e umidade alta"""
    if risco == "ALTO":
        return "Suor excessivo, mal-estar, assaduras, micoses"
    elif risco == "MÉDIO":
        return "Desconforto térmico, sudorese aumentada"
    else:
        return ""


def atencao_calor_seco(risco: str) -> str:
    """Riscos de saúde com calor seco"""
    if risco == "ALTO":
        return "Desidratação silenciosa, dor de garganta, ressecamento"
    elif risco == "MÉDIO":
        return "Desidratação gradual, garganta seca"
    else:
        return ""


def atencao_frio(risco: str) -> str:
    """Riscos de saúde relacionados ao frio"""
    if risco == "ALTO":
        return "Hipotermia, rigidez muscular, infecções respiratórias"
    elif risco == "MÉDIO":
        return "Dores musculares, maior risco de gripes"
    else:
        return ""


def atencao_frio_umido(risco: str) -> str:
    """Riscos com frio e umidade (chuva)"""
    if risco == "ALTO":
        return "Queda de imunidade, dores articulares, resfriados"
    elif risco == "MÉDIO":
        return "Desconforto, maior suscetibilidade a gripes"
    else:
        return ""


def atencao_tempo_seco(risco: str) -> str:
    """Riscos de saúde com baixa umidade do ar"""
    if risco == "ALTO":
        return "Nariz sangrando, olhos secos, irritação na garganta, pele ressecada"
    elif risco == "MÉDIO":
        return "Ressecamento das vias aéreas, desconforto nasal"
    else:
        return ""


def atencao_vento(risco: str) -> str:
    """Riscos com vento forte"""
    if risco == "ALTO":
        return "Irritação nos olhos, queda de temperatura corporal, partículas no ar"
    elif risco == "MÉDIO":
        return "Desconforto ocular, sensação térmica reduzida"
    else:
        return ""


def atencao_poluicao(risco: str) -> str:
    """Riscos de saúde com ar poluído"""
    if risco == "ALTO":
        return "Falta de ar, irritação ocular, tosse, crises respiratórias"
    elif risco == "MÉDIO":
        return "Desconforto respiratório, irritação leve das vias aéreas"
    else:
        return ""


def atencao_uv(risco: str) -> str:
    """Riscos de exposição ao UV"""
    if risco == "ALTO":
        return "Queimaduras, envelhecimento precoce da pele, risco de câncer de pele"
    elif risco == "MÉDIO":
        return "Danos cumulativos à pele, vermelhidão"
    else:
        return ""


def atencao_chuva(risco: str) -> str:
    """Riscos com chuva frequente"""
    if risco == "ALTO":
        return "Resfriados, fungos, frieiras, escorregões, contaminações"
    elif risco == "MÉDIO":
        return "Umidade excessiva, risco de fungos"
    else:
        return ""


def atencao_instabilidade(risco: str) -> str:
    """Riscos com mudanças bruscas de temperatura"""
    if risco == "ALTO":
        return "Dor de cabeça, rinite, pressão arterial instável, mal-estar"
    elif risco == "MÉDIO":
        return "Desconforto, adaptação do organismo"
    else:
        return ""
