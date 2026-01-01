# | Clima / Condição            | Fique atento a…                                                     | Cuidados recomendados                                                            |
# | :-------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------- |
# | **Calor intenso**           | Desidratação, queda de pressão, insolação, fadiga                   | Beber água com frequência, evitar sol entre 10–16h, roupas leves, protetor solar |
# | **Calor + umidade alta**    | Mal-estar, suor excessivo, micoses, assaduras                       | Roupas respiráveis, banho e secagem adequada, hidratação reforçada               |
# | **Frio intenso**            | Hipotermia, dores musculares, gripes                                | Agasalho em camadas, manter-se seco, alongar-se, bebidas quentes                 |
# | **Tempo seco**              | Nariz sangrando, olhos secos, irritação na garganta, pele ressecada | Umidificador ou bacia com água, hidratante corporal, beber mais água             |
# | **Chuva frequente**         | Resfriados, fungos, escorregões                                     | Evitar roupas molhadas, secar pés/calçados, atenção a pisos escorregadios        |
# | **Frio + chuva**            | Queda de imunidade, dores articulares                               | Manter-se aquecido e seco, alimentação reforçada                                 |
# | **Vento forte**             | Irritação nos olhos, queda de temperatura corporal                  | Óculos de proteção, casaco corta-vento                                           |
# | **Mudança brusca de clima** | Dor de cabeça, rinite, pressão instável                             | Rotina de sono regular, hidratação, evitar excessos                              |
# | **Clima poluído / fumaça**  | Falta de ar, irritação ocular, tosse                                | Evitar exercícios ao ar livre, lavar nariz (soro), ambientes ventilados          |
# | **Sol forte (UV alto)**     | Queimaduras, envelhecimento da pele, câncer de pele                 | Protetor solar, boné/chapéu, óculos escuros                                      |
# | **Frio seco**               | Lábios rachados, pele descamando                                    | Protetor labial, hidratantes, água                                               |
# | **Calor noturno**           | Sono ruim, cansaço                                                  | Ambiente ventilado, banho morno, roupas leves                                    |


def mensagem_calor(risco: str) -> str:
    if risco == "ALTO":
        return (
            "Calor intenso hoje. Evite o sol entre 10h e 16h, "
            "beba água com frequência e use roupas leves."
        )
    elif risco == "MÉDIO":
        return (
            "O dia está quente. Hidrate-se bem e reduza esforço físico "
            "nos horários mais quentes."
        )
    else:
        return "Temperatura confortável. Mantenha a hidratação ao longo do dia."


def mensagem_calor_umido(risco: str) -> str:
    if risco == "ALTO":
        return (
            "Calor com umidade elevada. Use roupas respiráveis, "
            "mantenha a pele seca e reforce a hidratação."
        )
    elif risco == "MÉDIO":
        return (
            "O clima está abafado. Prefira roupas leves e faça pausas "
            "para se refrescar."
        )
    else:
        return ""


def mensagem_frio(risco: str) -> str:
    if risco == "ALTO":
        return (
            "Frio intenso e úmido. Mantenha-se aquecido e seco, "
            "evite roupas molhadas e reforce a alimentação."
        )
    elif risco == "MÉDIO":
        return (
            "Temperatura baixa hoje. Use agasalhos em camadas "
            "e evite exposição prolongada."
        )
    else:
        return ""


def mensagem_tempo_seco(risco: str) -> str:
    if risco == "ALTO":
        return (
            "O ar está muito seco. Beba mais água, use hidratante corporal "
            "e, se possível, umidifique o ambiente."
        )
    elif risco == "MÉDIO":
        return "Umidade baixa hoje. Hidrate-se bem e evite ambientes muito fechados."
    else:
        return ""


def mensagem_vento(risco: str) -> str:
    if risco == "ALTO":
        return (
            "Vento forte hoje. Proteja os olhos e use casaco corta-vento "
            "se for sair."
        )
    elif risco == "MÉDIO":
        return "Vento moderado. Um agasalho leve pode ajudar no conforto."
    else:
        return ""


def mensagem_poluicao(risco: str) -> str:
    if risco == "ALTO":
        return (
            "Qualidade do ar ruim. Evite exercícios ao ar livre "
            "e, se possível, permaneça em ambientes ventilados."
        )
    elif risco == "MÉDIO":
        return (
            "O ar está mais carregado. Pessoas sensíveis devem reduzir esforço físico."
        )
    else:
        return "Qualidade do ar boa para atividades ao ar livre."


def mensagem_geral(risco_geral: str) -> str:
    if risco_geral == "ALTO":
        return (
            "O clima de hoje exige atenção. Priorize hidratação, descanso "
            "e proteção ao sair de casa."
        )
    elif risco_geral == "MÉDIO":
        return (
            "Algumas condições exigem cuidado hoje. Observe seu corpo "
            "e evite excessos."
        )
    else:
        return "Condições favoráveis hoje. Aproveite com moderação."
