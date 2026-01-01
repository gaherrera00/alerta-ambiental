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


def risco_calor(feels_like: float) -> str:
    if feels_like >= 35:
        return "ALTO"
    elif feels_like >= 30:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_calor_umido(feels_like: float, umidade: int) -> str:
    if feels_like >= 30 and umidade >= 70:
        return "ALTO"
    elif feels_like >= 28 and umidade >= 60:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_frio(temp: float, chuva: bool) -> str:
    if temp <= 10 and chuva:
        return "ALTO"
    elif temp <= 12:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_tempo_seco(umidade: int) -> str:
    if umidade < 30:
        return "ALTO"
    elif umidade < 40:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_vento(vento_kmh: float) -> str:
    if vento_kmh >= 40:
        return "ALTO"
    elif vento_kmh >= 25:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_poluicao(aqi: int, pm2_5: float) -> str:
    if aqi >= 4 or pm2_5 >= 35:
        return "ALTO"
    elif aqi == 3 or pm2_5 >= 25:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_instabilidade(temp_atual: float, temp_anterior: float) -> str:
    variacao = abs(temp_atual - temp_anterior)

    if variacao >= 8:
        return "ALTO"
    elif variacao >= 5:
        return "MÉDIO"
    else:
        return "BAIXO"


def risco_geral(riscos: list[str]) -> str:
    if "ALTO" in riscos:
        return "ALTO"
    elif "MÉDIO" in riscos:
        return "MÉDIO"
    else:
        return "BAIXO"
