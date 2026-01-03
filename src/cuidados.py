
def cuidado_calor(risco: str) -> str:
    """Cuidados recomendados para calor"""
    if risco == "ALTO":
        return (
            "Beber água regularmente (mesmo sem sede), evitar sol entre 10h–16h, "
            "usar roupas claras e leves, aplicar protetor solar, fazer pausas à sombra"
        )
    elif risco == "MÉDIO":
        return (
            "Hidrate-se com frequência, reduza esforço físico nos horários mais quentes, "
            "prefira locais ventilados"
        )
    else:
        return "Mantenha hidratação regular ao longo do dia"


def cuidado_calor_umido(risco: str) -> str:
    """Cuidados com calor e umidade"""
    if risco == "ALTO":
        return (
            "Use tecidos respiráveis (algodão, linho), troque roupas molhadas rapidamente, "
            "tome banhos regulares e seque bem a pele, reforce a hidratação"
        )
    elif risco == "MÉDIO":
        return (
            "Prefira roupas leves e respiráveis, mantenha-se em locais ventilados, "
            "hidrate-se bem"
        )
    else:
        return ""


def cuidado_calor_seco(risco: str) -> str:
    """Cuidados com calor seco"""
    if risco == "ALTO":
        return (
            "Aumente ingestão de líquidos além do habitual, umidifique ambientes, "
            "evite bebidas alcoólicas que desidratam"
        )
    elif risco == "MÉDIO":
        return "Beba mais água que o normal, mantenha ambientes arejados"
    else:
        return ""


def cuidado_frio(risco: str) -> str:
    """Cuidados com frio"""
    if risco == "ALTO":
        return (
            "Vista agasalhos em camadas, mantenha-se seco, tome bebidas quentes, "
            "faça alongamentos, evite exposição prolongada"
        )
    elif risco == "MÉDIO":
        return (
            "Use agasalhos adequados, mantenha extremidades aquecidas, "
            "evite mudanças bruscas de temperatura"
        )
    else:
        return ""


def cuidado_frio_umido(risco: str) -> str:
    """Cuidados com frio e chuva"""
    if risco == "ALTO":
        return (
            "Mantenha-se aquecido e seco, troque roupas molhadas imediatamente, "
            "reforce alimentação, use calçados impermeáveis"
        )
    elif risco == "MÉDIO":
        return "Evite roupas molhadas, mantenha-se aquecido, seque bem pés e calçados"
    else:
        return ""


def cuidado_tempo_seco(risco: str) -> str:
    """Cuidados com ar seco"""
    if risco == "ALTO":
        return (
            "Use umidificador ou coloque bacias com água em casa, "
            "aplique hidratante corporal, lave nariz com soro fisiológico, "
            "beba mais água que o habitual"
        )
    elif risco == "MÉDIO":
        return (
            "Hidrate-se bem, use hidratante labial e corporal, "
            "evite ambientes muito fechados"
        )
    else:
        return ""


def cuidado_vento(risco: str) -> str:
    """Cuidados com vento forte"""
    if risco == "ALTO":
        return (
            "Use óculos de proteção, vista casaco corta-vento, "
            "proteja vias respiratórias se houver poeira"
        )
    elif risco == "MÉDIO":
        return "Um agasalho leve ou corta-vento pode ajudar no conforto"
    else:
        return ""


def cuidado_poluicao(risco: str) -> str:
    """Cuidados com ar poluído"""
    if risco == "ALTO":
        return (
            "Evite exercícios ao ar livre, lave o nariz com soro fisiológico, "
            "mantenha ambientes ventilados mas com janelas fechadas em horários de pico, "
            "considere usar máscara PFF2"
        )
    elif risco == "MÉDIO":
        return (
            "Pessoas sensíveis devem reduzir esforço físico ao ar livre, "
            "lave nariz com soro se sentir irritação"
        )
    else:
        return "Qualidade do ar favorável para atividades ao ar livre"


def cuidado_uv(risco: str) -> str:
    """Cuidados com radiação UV"""
    if risco == "ALTO":
        return (
            "Use protetor solar FPS 30+ (reaplique a cada 2h), "
            "use boné/chapéu e óculos escuros, evite exposição entre 10h–16h, "
            "prefira sombra"
        )
    elif risco == "MÉDIO":
        return (
            "Aplique protetor solar antes de sair, use óculos escuros, "
            "evite exposição prolongada ao sol"
        )
    else:
        return "Use protetor solar básico mesmo em dias nublados"


def cuidado_chuva(risco: str) -> str:
    """Cuidados com chuva"""
    if risco == "ALTO":
        return (
            "Evite contato com água de enchentes, seque pés e calçados completamente, "
            "troque roupas molhadas, atenção a pisos escorregadios, "
            "higienize ferimentos imediatamente"
        )
    elif risco == "MÉDIO":
        return (
            "Mantenha-se seco, atenção a pisos molhados, "
            "seque calçados adequadamente"
        )
    else:
        return ""


def cuidado_instabilidade(risco: str) -> str:
    """Cuidados com mudanças bruscas de clima"""
    if risco == "ALTO":
        return (
            "Mantenha rotina de sono regular, hidrate-se bem, "
            "evite excessos físicos, adapte vestuário gradualmente"
        )
    elif risco == "MÉDIO":
        return (
            "Observe como seu corpo reage, ajuste roupas conforme necessário, "
            "mantenha-se hidratado"
        )
    else:
        return ""


def cuidado_geral(risco: str) -> str:
    """Mensagem geral de cuidado"""
    if risco == "ALTO":
        return (
            "O clima exige atenção especial hoje. Priorize sua saúde: "
            "hidratação, descanso adequado e proteção ao sair"
        )
    elif risco == "MÉDIO":
        return (
            "Algumas condições climáticas exigem cuidado. "
            "Observe seu corpo e evite excessos"
        )
    else:
        return "Condições favoráveis. Aproveite o dia com moderação"
