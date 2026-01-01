# importacao de bibliotecas
import streamlit as st

from src.services.weather import tempo
from src.services.air_quality import qualidade_ar

from src.risk import (
    risco_calor,
    risco_calor_umido,
    risco_tempo_seco,
    risco_poluicao,
    risco_geral,
)

from src.messages import (
    mensagem_calor,
    mensagem_calor_umido,
    mensagem_tempo_seco,
    mensagem_poluicao,
    mensagem_geral,
)

from src.utils.aqi_mapper import interpretar_aqi


# config da página
st.set_page_config(page_title="Alerta Ambiental", layout="centered")

st.title("🌍 Alerta Ambiental")
st.write("Informações simples para cuidar da sua saúde conforme o clima e o ar.")

# Entrada do usuário
cidade = st.text_input("Digite o nome da cidade", placeholder="Ex: São Paulo")

# Botão buscar
if st.button("Buscar informações"):
    if not cidade:
        st.warning("Digite uma cidade")
    else:
        try:
            clima = tempo(cidade)
            # Métricas de clima
            st.success(f"Condições em {clima['cidade']}")

            col1, col2, col3 = st.columns(3)

            col1.metric("Temperatura", f"{clima['temperatura']} °C")
            col2.metric("Sensação térmica", f"{clima['sensacao_termica']} °C")
            col3.metric("Umidade", f"{clima['umidade']} %")

            # Qualidade do ar
            ar = qualidade_ar(clima["lat"], clima["lon"])

            st.divider()
            st.subheader("Qualidade do ar")

            st.metric("Qualidade do ar", interpretar_aqi(ar["aqi"]))

            # Cálculo dos riscos
            r_calor = risco_calor(clima["sensacao_termica"])
            r_calor_umido = risco_calor_umido(
                clima["sensacao_termica"], clima["umidade"]
            )
            r_seco = risco_tempo_seco(clima["umidade"])
            r_ar = risco_poluicao(ar["aqi"], ar["pm2_5"])

            risco_final = risco_geral(
                [
                    r_calor,
                    r_calor_umido,
                    r_seco,
                    r_ar,
                ]
            )

            # Mensagens de saúde
            st.subheader("Recomendações")

            mensagens = [
                mensagem_calor(r_calor),
                mensagem_calor_umido(r_calor_umido),
                mensagem_tempo_seco(r_seco),
                mensagem_poluicao(r_ar),
            ]

            for msg in mensagens:
                if msg:
                    st.info(msg)

            st.divider()
            st.success(mensagem_geral(risco_final))

        # Erro
        except Exception:
            st.error(
                "Não foi possível obter os dados no momento. "
                "Verifique a cidade ou tente novamente mais tarde."
            )
