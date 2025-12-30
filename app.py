from src.weather import tempo
import streamlit as st

st.set_page_config(page_title="Clima em tempo real", layout="centered")

st.title("🌦️ Clima em tempo real")
st.write("Consulte o clima atual da sua cidade")

cidade = st.text_input("Digite o nome da cidade", placeholder="Ex: São Paulo")

if st.button("Buscar clima"):
    if not cidade:
        st.warning("Digite uma cidade")
    else:
        clima = tempo(cidade)

        if clima:
            st.success(f"Clima em {clima['cidade']}")

            col1, col2, col3 = st.columns(3)

            col1.metric("Temperatura", f"{clima['temperatura']} °C")
            col2.metric("Sensação Termica", f"{clima['sensacao_termica']} °C")
            col3.metric("Umidade", f"{clima['umidade']} %")

            st.divider()

            st.write(f"**Tempo:** {clima['descricao_tempo']}")
            st.write(f"**Vento:** {clima['vento_kmh']} km/h")
            st.write(f"**Visibilidade:** {clima['visibilidade_m']} m")
        else:
            st.error("Não foi possível obter os dados. Verifique a cidade.")
