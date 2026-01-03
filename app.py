# IMPORTAÇÕES

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

from src.utils.aqi_mapper import interpretar_aqi


# FUNÇÕES AUXILIARES


def get_risco_emoji(risco: str) -> str:
    return {"BAIXO": "🟢", "MÉDIO": "🟡", "ALTO": "🔴"}.get(risco, "⚪")


def get_risco_color(risco: str) -> str:
    return {"BAIXO": "green", "MÉDIO": "orange", "ALTO": "red"}.get(risco, "gray")


# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title="Alerta Ambiental",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# CSS CUSTOMIZADO

st.markdown(
    """
<style>
    /* Esconder menu e footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Container principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Cards com fundo escuro */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    div[data-testid="stMetric"] label {
        color: #b3c9ff !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: white !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: #8fb9ff !important;
    }
    
    /* Títulos */
    h1 {
        color: #1e3c72;
        font-weight: 700;
    }
    
    h2, h3 {
        color: #2a5298;
        font-weight: 600;
    }
    
    /* Alert boxes personalizados */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
    }
</style>
""",
    unsafe_allow_html=True,
)


# HEADER

st.title("🌍 Alerta Ambiental")
st.markdown("### Informações climáticas e recomendações de saúde")


# INPUT

col_input, col_button = st.columns([4, 1])
with col_input:
    cidade = st.text_input(
        "Digite a cidade",
        placeholder="Ex: São Paulo, Rio de Janeiro, Curitiba",
        label_visibility="collapsed",
    )
with col_button:
    buscar = st.button("Buscar", use_container_width=True, type="secondary")

st.divider()


# PROCESSAMENTO

if buscar:
    if not cidade:
        st.warning("⚠️ Digite o nome de uma cidade para continuar.")
    else:
        try:
            with st.spinner("🔄 Buscando informações climáticas..."):
                clima = tempo(cidade)
                ar = qualidade_ar(clima["lat"], clima["lon"])
                uv = get_uv_index(clima["lat"], clima["lon"])

            # CABEÇALHO COM CIDADE

            st.markdown(f"## 📍 {clima['cidade']}")
            st.caption(f"🌤️ {clima['descricao_tempo'].capitalize()}")

            st.markdown("---")

            # MÉTRICAS PRINCIPAIS (GRID 4x2)

            st.markdown("### 📊 Condições Atuais")

            # Linha 1
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    label="🌡️ Temperatura",
                    value=f"{clima['temperatura']:.0f}°C",
                    delta=f"Sensação: {clima['sensacao_termica']:.0f}°C",
                )

            with col2:
                st.metric(
                    label="💧 Umidade",
                    value=f"{clima['umidade']}%",
                    delta="Umidade relativa",
                )

            with col3:
                st.metric(
                    label="🌬️ Vento",
                    value=f"{clima['vento_kmh']:.0f} km/h",
                    delta="Velocidade",
                )

            with col4:
                uv_value = f"{uv:.1f}" if uv else "N/D"
                st.metric(label="☀️ Índice UV", value=uv_value, delta="Radiação solar")

            # Linha 2
            col5, col6, col7, col8 = st.columns(4)

            with col5:
                st.metric(
                    label="😷 Qualidade do Ar",
                    value=interpretar_aqi(ar["aqi"]),
                    delta=f"AQI: {ar['aqi']}",
                )

            with col6:
                st.metric(
                    label="🌫️ PM2.5",
                    value=f"{ar['pm2_5']:.0f} µg/m³",
                    delta="Material particulado",
                )

            with col7:
                st.metric(
                    label="👁️ Visibilidade",
                    value=f"{clima['visibilidade_m']/1000:.1f} km",
                    delta="Alcance visual",
                )

            with col8:
                st.metric(
                    label="🏜️ PM10",
                    value=f"{ar['pm10']:.0f} µg/m³",
                    delta="Partículas maiores",
                )

            st.markdown("---")

            # CÁLCULO DE RISCOS

            r_calor = risco_calor(clima["sensacao_termica"])
            r_calor_umido = risco_calor_umido(
                clima["sensacao_termica"], clima["umidade"]
            )
            r_seco = risco_tempo_seco(clima["umidade"])
            r_ar = risco_poluicao(ar["aqi"], ar["pm2_5"])
            r_vento = risco_vento(clima["vento_kmh"])
            r_uv = risco_uv(uv) if uv else "BAIXO"

            risco_final = risco_geral(
                [r_calor, r_calor_umido, r_seco, r_ar, r_vento, r_uv]
            )

            # ALERTA GERAL

            st.markdown("### 🚨 Status Geral de Saúde")

            emoji_geral = get_risco_emoji(risco_final)
            color_geral = get_risco_color(risco_final)

            if risco_final == "ALTO":
                st.error(f"{emoji_geral} **ATENÇÃO:** {cuidado_geral(risco_final)}")
            elif risco_final == "MÉDIO":
                st.warning(f"{emoji_geral} **CUIDADO:** {cuidado_geral(risco_final)}")
            else:
                st.success(f"{emoji_geral} **TRANQUILO:** {cuidado_geral(risco_final)}")

            st.markdown("---")

            # ALERTAS DETALHADOS (GRID 2x3)

            st.markdown("### ⚡ Análise Detalhada dos Riscos")

            alertas = [
                ("🌡️ Calor", r_calor, atencao_calor(r_calor), cuidado_calor(r_calor)),
                (
                    "💧 Calor Úmido",
                    r_calor_umido,
                    atencao_calor_umido(r_calor_umido),
                    cuidado_calor_umido(r_calor_umido),
                ),
                (
                    "🏜️ Ar Seco",
                    r_seco,
                    atencao_tempo_seco(r_seco),
                    cuidado_tempo_seco(r_seco),
                ),
                (
                    "😷 Qualidade do Ar",
                    r_ar,
                    atencao_poluicao(r_ar),
                    cuidado_poluicao(r_ar),
                ),
                ("🌬️ Vento", r_vento, atencao_vento(r_vento), cuidado_vento(r_vento)),
                ("☀️ Radiação UV", r_uv, atencao_uv(r_uv), cuidado_uv(r_uv)),
            ]

            # Filtrar alertas relevantes
            alertas_relevantes = [
                (nome, risco, atencao, cuidado)
                for nome, risco, atencao, cuidado in alertas
                if risco != "BAIXO" or cuidado
            ]

            if alertas_relevantes:
                # Grid 2 colunas
                col_left, col_right = st.columns(2)

                for i, (nome, risco, atencao, cuidado) in enumerate(alertas_relevantes):
                    emoji = get_risco_emoji(risco)

                    with col_left if i % 2 == 0 else col_right:
                        with st.container():
                            # Título do alerta
                            st.markdown(f"#### {nome} {emoji} **{risco}**")

                            # O que pode acontecer
                            if atencao:
                                st.markdown("**⚠️ Fique atento:**")
                                st.info(atencao)

                            # O que fazer
                            if cuidado:
                                st.markdown("**✅ Recomendações:**")
                                if risco == "ALTO":
                                    st.error(cuidado)
                                elif risco == "MÉDIO":
                                    st.warning(cuidado)
                                else:
                                    st.success(cuidado)

                            st.markdown("")  # Espaçamento
            else:
                st.success(
                    "🎉 **Excelente!** Todas as condições climáticas estão favoráveis hoje."
                )

            # DETALHES TÉCNICOS (EXPANDER)

            st.markdown("---")

            with st.expander("🔬 Ver Detalhes Técnicos Completos"):
                st.markdown("#### 🌡️ Dados Climáticos")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Temperatura Real", f"{clima['temperatura']:.1f}°C")
                col2.metric("Sensação Térmica", f"{clima['sensacao_termica']:.1f}°C")
                col3.metric("Umidade Relativa", f"{clima['umidade']}%")
                col4.metric("Velocidade do Vento", f"{clima['vento_kmh']} km/h")

                st.markdown("#### 🌫️ Qualidade do Ar")
                col5, col6, col7, col8 = st.columns(4)
                col5.metric("AQI", ar["aqi"])
                col6.metric("PM2.5", f"{ar['pm2_5']:.1f} µg/m³")
                col7.metric("PM10", f"{ar['pm10']:.1f} µg/m³")
                col8.metric("O₃", f"{ar['o3']:.1f} µg/m³")

                col9, col10 = st.columns(2)
                col9.metric("CO", f"{ar['co']:.1f} µg/m³")
                col10.metric("NO₂", f"{ar['no2']:.1f} µg/m³")

        except Exception as e:
            st.error("❌ **Erro ao buscar dados**")
            st.error(
                f"Não foi possível obter informações para '{cidade}'. Verifique o nome da cidade."
            )
            with st.expander("🐛 Detalhes técnicos do erro"):
                st.code(str(e))
