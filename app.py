# ===============================
# IMPORTAÇÕES
# ===============================

import streamlit as st

from src.services.weather import tempo
from src.services.air_quality import qualidade_ar
from src.services.uv import get_uv_index

from src.risk import (
    risco_calor,
    risco_calor_umido,
    risco_tempo_seco,
    risco_poluicao,
    risco_uv,
    risco_vento,
    risco_geral,
)

from src.atencao import (
    atencao_calor,
    atencao_calor_umido,
    atencao_tempo_seco,
    atencao_poluicao,
    atencao_uv,
    atencao_vento,
)

from src.cuidados import (
    cuidado_calor,
    cuidado_calor_umido,
    cuidado_tempo_seco,
    cuidado_poluicao,
    cuidado_uv,
    cuidado_vento,
    cuidado_geral,
)

from src.explicacoes import (
    explicacao_calor,
    explicacao_calor_umido,
    explicacao_tempo_seco,
    explicacao_poluicao,
    explicacao_uv,
    explicacao_vento,
    explicacao_hidratacao,
    explicacao_grupos_vulneraveis,
)

from src.utils.aqi_mapper import interpretar_aqi
from src.utils.uv_mapper import interpretar_uv


# ===============================
# FUNÇÕES AUXILIARES
# ===============================


def get_risco_color(risco: str) -> str:
    return {
        "BAIXO": "success",
        "MÉDIO": "warning",
        "ALTO": "error",
    }.get(risco, "info")


# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================

st.set_page_config(
    page_title="Alerta Ambiental",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ===============================
# CSS CUSTOMIZADO
# ===============================

st.markdown(
    """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(180deg, #ffffff 0%, #f7f9fc 100%);
        padding: 1.4rem;
        border-radius: 14px;
        border: 1px solid #eef1f6;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
    }

    div[data-testid="stMetric"] label {
        color: #6b7280 !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    h1 {
        color: #111827;
        font-weight: 700;
    }

    h2, h3, h4 {
        color: #1f2937;
        font-weight: 600;
    }

    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
    }
    
    /* Estilo para as explicações científicas */
    .explicacao-cientifica {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 4px solid #0ea5e9;
        margin-top: 0.8rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        line-height: 1.6;
        color: black;
    }
</style>
""",
    unsafe_allow_html=True,
)


# ===============================
# HEADER
# ===============================

st.title("Alerta Ambiental")
st.markdown(
    "Informações climáticas atualizadas com foco em bem-estar, saúde e atividades ao ar livre."
)


# ===============================
# INPUT
# ===============================

col_input, col_button = st.columns([4, 1])

with col_input:
    cidade = st.text_input(
        "Cidade",
        placeholder="Ex: São Paulo, Rio de Janeiro, Curitiba",
        label_visibility="collapsed",
    )

with col_button:
    buscar = st.button("Ver condições do dia", use_container_width=True)

st.divider()


# ===============================
# PROCESSAMENTO
# ===============================

if buscar:
    if not cidade:
        st.warning("Digite o nome de uma cidade para continuar.")
    else:
        try:
            with st.spinner("Buscando informações climáticas..."):
                clima = tempo(cidade)
                ar = qualidade_ar(clima["lat"], clima["lon"])
                uv = get_uv_index(clima["lat"], clima["lon"])

            # ===============================
            # CABEÇALHO DA CIDADE
            # ===============================

            st.markdown(f"## {clima['cidade']}")
            st.caption(clima["descricao_tempo"].capitalize())

            st.markdown("<br>", unsafe_allow_html=True)

            # ===============================
            # CONDIÇÕES ATUAIS
            # ===============================

            st.markdown("### Como está o dia agora")
            st.caption("Resumo rápido das condições que impactam seu conforto e saúde.")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Temperatura",
                f"{clima['temperatura']:.0f}°C",
                f"Sensação: {clima['sensacao_termica']:.0f}°C",
            )
            col2.metric("Umidade", f"{clima['umidade']}%", "Umidade relativa")
            col3.metric("Vento", f"{clima['vento_kmh']:.0f} km/h", "Velocidade média")

            # UV com interpretação e valor numérico
            uv_interpretado = interpretar_uv(uv)
            uv_valor = f"Índice: {uv:.1f}" if uv is not None else "Sem dados"
            col4.metric("Índice UV", uv_interpretado, uv_valor)

            col5, col6, col7, col8 = st.columns(4)

            col5.metric(
                "Qualidade do ar",
                interpretar_aqi(ar["aqi"]),
                f"AQI: {ar['aqi']}",
            )
            col6.metric("PM2.5", f"{ar['pm2_5']:.0f} µg/m³", "Partículas finas")
            col7.metric(
                "Visibilidade",
                f"{clima['visibilidade_m']/1000:.1f} km",
                "Alcance visual",
            )
            col8.metric("PM10", f"{ar['pm10']:.0f} µg/m³", "Partículas maiores")

            st.divider()

            # ===============================
            # CÁLCULO DE RISCOS
            # ===============================

            r_calor = risco_calor(clima["sensacao_termica"])
            r_calor_umido = risco_calor_umido(
                clima["sensacao_termica"], clima["umidade"]
            )
            r_seco = risco_tempo_seco(clima["umidade"])
            r_ar = risco_poluicao(ar["aqi"], ar["pm2_5"])
            r_vento = risco_vento(clima["vento_kmh"])
            r_uv = risco_uv(uv) if uv is not None else "BAIXO"

            risco_final = risco_geral(
                [r_calor, r_calor_umido, r_seco, r_ar, r_vento, r_uv]
            )

            # ===============================
            # AVALIAÇÃO GERAL
            # ===============================

            st.markdown("### Avaliação geral de hoje")
            st.caption(
                "Com base no clima, qualidade do ar e radiação solar, "
                "avaliamos o impacto no seu dia."
            )

            if risco_final == "ALTO":
                st.error(cuidado_geral(risco_final))
            elif risco_final == "MÉDIO":
                st.warning(cuidado_geral(risco_final))
            else:
                st.success(cuidado_geral(risco_final))

            st.divider()

            # ===============================
            # EXPLICAÇÕES EDUCATIVAS GERAIS
            # ===============================

            with st.expander("💡 Informações importantes sobre saúde ambiental"):
                st.markdown(explicacao_hidratacao())
                st.markdown("---")
                st.markdown(explicacao_grupos_vulneraveis())

            st.divider()

            # ===============================
            # ANÁLISE DETALHADA COM EXPLICAÇÕES
            # ===============================

            st.markdown("### O que merece atenção hoje")

            alertas = [
                (
                    "Calor",
                    r_calor,
                    atencao_calor(r_calor),
                    cuidado_calor(r_calor),
                    explicacao_calor(r_calor),
                ),
                (
                    "Calor úmido",
                    r_calor_umido,
                    atencao_calor_umido(r_calor_umido),
                    cuidado_calor_umido(r_calor_umido),
                    explicacao_calor_umido(r_calor_umido),
                ),
                (
                    "Ar seco",
                    r_seco,
                    atencao_tempo_seco(r_seco),
                    cuidado_tempo_seco(r_seco),
                    explicacao_tempo_seco(r_seco),
                ),
                (
                    "Qualidade do ar",
                    r_ar,
                    atencao_poluicao(r_ar),
                    cuidado_poluicao(r_ar),
                    explicacao_poluicao(r_ar),
                ),
                (
                    "Vento",
                    r_vento,
                    atencao_vento(r_vento),
                    cuidado_vento(r_vento),
                    explicacao_vento(r_vento),
                ),
                (
                    "Radiação UV",
                    r_uv,
                    atencao_uv(r_uv),
                    cuidado_uv(r_uv),
                    explicacao_uv(r_uv),
                ),
            ]

            # Filtra apenas alertas relevantes
            alertas = [a for a in alertas if a[1] != "BAIXO" or a[3]]

            if alertas:
                col_left, col_right = st.columns(2)

                for i, (nome, risco, atencao, cuidado, explicacao) in enumerate(
                    alertas
                ):
                    with col_left if i % 2 == 0 else col_right:
                        st.markdown(f"#### {nome}")
                        st.caption(f"Nível de atenção: {risco}")

                        if atencao:
                            st.info(f"**O que pode acontecer:** {atencao}")

                        if cuidado:
                            getattr(st, get_risco_color(risco))(
                                f"**Como se proteger:** {cuidado}"
                            )

                        # Adiciona explicação científica se disponível
                        if explicacao:
                            st.markdown(
                                f'<div class="explicacao-cientifica">{explicacao}</div>',
                                unsafe_allow_html=True,
                            )

                        st.markdown("<br>", unsafe_allow_html=True)
            else:
                st.success(
                    "As condições estão favoráveis para a maioria das atividades."
                )

            # ===============================
            # DETALHES TÉCNICOS
            # ===============================

            st.divider()

            with st.expander("📊 Ver dados técnicos completos"):
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Temperatura", f"{clima['temperatura']:.1f}°C")
                col2.metric("Sensação térmica", f"{clima['sensacao_termica']:.1f}°C")
                col3.metric("Umidade", f"{clima['umidade']}%")
                col4.metric("Vento", f"{clima['vento_kmh']} km/h")

                col5, col6, col7, col8 = st.columns(4)
                col5.metric("AQI", ar["aqi"])
                col6.metric("UV Index", f"{uv:.1f}" if uv is not None else "N/D")
                col7.metric("PM2.5", f"{ar['pm2_5']:.1f} µg/m³")
                col8.metric("PM10", f"{ar['pm10']:.1f} µg/m³")

                col9, col10, col11, col12 = st.columns(4)
                col9.metric("O₃", f"{ar['o3']:.1f} µg/m³")
                col10.metric("CO", f"{ar['co']:.1f} µg/m³")
                col11.metric("NO₂", f"{ar['no2']:.1f} µg/m³")
                col12.metric("Visibilidade", f"{clima['visibilidade_m']} m")

        except Exception as e:
            st.error("Não foi possível obter as informações da cidade.")
            with st.expander("Detalhes técnicos"):
                st.code(str(e))
