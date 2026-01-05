"""
Explicações científicas sobre o porquê das recomendações de saúde
Baseado em diretrizes da OMS e literatura médica
"""


def explicacao_calor(risco: str) -> str:
    """Explica por que o calor é um risco à saúde"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: Quando a temperatura sobe, seu corpo usa o suor "
            "como principal mecanismo de resfriamento. A evaporação do suor consome calor "
            "da pele, ajudando a manter sua temperatura interna em ~37°C. Porém, essa "
            "evaporação causa perda de água e sais minerais. Se a perda ultrapassar 2% do "
            "seu peso corporal, você pode ter queda de desempenho físico, fadiga e até "
            "exaustão térmica. Em casos extremos (acima de 40°C de temperatura corporal), "
            "pode ocorrer insolação, uma emergência médica grave."
        )
    return ""


def explicacao_calor_umido(risco: str) -> str:
    """Explica por que calor + umidade é problemático"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: Quando a umidade está alta (acima de 70%), o ar "
            "já está saturado de vapor d'água. Isso dificulta a evaporação do seu suor, que "
            "é o principal mecanismo de resfriamento do corpo. Você continua suando, mas sem "
            "o efeito refrescante da evaporação. Isso leva à perda excessiva de líquidos sem "
            "resfriamento adequado, aumentando o risco de desidratação, exaustão térmica e "
            "proliferação de fungos na pele úmida."
        )
    return ""


def explicacao_tempo_seco(risco: str) -> str:
    """Explica por que a baixa umidade é prejudicial"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: Suas vias respiratórias são revestidas por uma "
            "camada de muco que filtra, umidifica e aquece o ar que você respira. Quando a "
            "umidade do ar cai abaixo de 40%, esse muco evapora e fica mais espesso, perdendo "
            "a capacidade de proteger contra vírus, bactérias e partículas irritantes. Isso "
            "facilita infecções respiratórias, sangramento nasal (pela ruptura de vasos na "
            "mucosa ressecada) e irritações nos olhos. A OMS considera alerta quando a umidade "
            "fica abaixo de 30%."
        )
    return ""


def explicacao_poluicao(risco: str) -> str:
    """Explica por que a poluição do ar é prejudicial"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: Partículas PM2.5 são tão pequenas (2,5 micrômetros) "
            "que conseguem penetrar profundamente nos pulmões e até entrar na corrente sanguínea. "
            "A OMS reduziu recentemente seus limites recomendados para apenas 5 µg/m³ anuais, pois "
            "evidências mostram que mesmo exposições baixas aumentam o risco de doenças "
            "cardiovasculares, respiratórias e até câncer de pulmão. Em dias de alta poluição, "
            "pessoas com asma, bronquite ou doenças cardíacas sofrem agravamento dos sintomas."
        )
    return ""


def explicacao_uv(risco: str) -> str:
    """Explica por que a radiação UV é prejudicial"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: A radiação ultravioleta (UV) é um tipo de radiação "
            "eletromagnética que danifica o DNA das células da pele. A exposição repetida causa "
            "envelhecimento precoce e aumenta significativamente o risco de câncer de pele "
            "(melanoma e carcinomas). Mesmo em dias nublados, até 80% dos raios UV atravessam as "
            "nuvens. A OMS recomenda proteção sempre que o índice UV for 3 ou superior. Superfícies "
            "como água, areia e neve refletem e amplificam a radiação, aumentando a exposição."
        )
    return ""


def explicacao_vento(risco: str) -> str:
    """Explica por que o vento forte impacta a saúde"""
    if risco in ["ALTO", "MÉDIO"]:
        return (
            "Por que isso importa: Vento forte acelera a evaporação do suor e da umidade "
            "da pele, aumentando a sensação de frio (efeito 'wind chill'). Isso pode levar à "
            "hipotermia mais rapidamente em dias frios. Além disso, o vento carrega partículas de "
            "poeira, pólen e poluentes, aumentando a concentração desses irritantes no ar e "
            "causando irritação nos olhos, nariz e garganta. Pessoas com alergias ou asma são "
            "particularmente sensíveis."
        )
    return ""


def explicacao_hidratacao() -> str:
    """Explicação geral sobre a importância da hidratação"""
    return (
        "Hidratação é fundamental: Seu corpo é ~60-70% água. Você perde água "
        "constantemente pela respiração, suor, urina e fezes. Em dias quentes ou secos, "
        "essas perdas aumentam. A desidratação começa com sintomas leves (sede, fadiga, "
        "dor de cabeça) mas pode evoluir para confusão mental, queda de pressão e, em casos "
        "graves, falência de órgãos. A regra prática da OMS é: multiplique seu peso por 35 ml. "
        "Uma pessoa de 70kg deve beber ~2,5L/dia, aumentando em dias quentes ou durante exercícios."
    )


def explicacao_grupos_vulneraveis() -> str:
    """Explica por que certos grupos são mais vulneráveis"""
    return (
        "Grupos vulneráveis: Crianças têm maior proporção entre superfície corporal "
        "e peso, produzem mais calor durante atividades e suam menos que adultos. Seu mecanismo "
        "de sede ainda não é totalmente desenvolvido, então desidratam mais facilmente. Idosos "
        "têm menor percepção de sede (barorreceptores menos sensíveis), menor reserva hídrica e "
        "termorregulação menos eficiente. Pessoas com doenças crônicas (diabetes, hipertensão, "
        "doenças cardíacas/renais) têm sistemas de compensação comprometidos e maior risco de "
        "complicações."
    )
