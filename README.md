# ⚠️ Alerta Ambiental
## Análise de Condições Climáticas e Recomendações de Saúde
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=for-the-badge)](https://github.com/seu-usuario/seu-repo)

---

### 💡 Visão Geral do Projeto

O **Alerta Ambiental** é uma aplicação em Python desenvolvida para transformar dados meteorológicos em tempo real em **orientações práticas de saúde pública**. Seu foco principal é a proteção de populações vulneráveis (idosos, crianças e pessoas com doenças crônicas) contra os riscos associados a condições climáticas extremas, como ondas de calor ou frio intenso.

O projeto visa ajudar usuários a **entender melhor os riscos** e receber **orientações práticas de cuidados com a saúde** com base nos dados coletados.

---

### 🎯 Impacto e Relevância: Saúde Pública e Clima

Em um cenário de mudanças climáticas e eventos extremos cada vez mais frequentes, a capacidade de traduzir dados ambientais complexos em ações preventivas é crucial.

Este projeto demonstra a aplicação direta de dados para:
*   **Informar Decisões de Saúde Pública:** Vai além da simples previsão do tempo, oferecendo um *sistema de suporte à decisão* baseado em riscos de saúde.
*   **Prevenção de Riscos:** Ajuda a mitigar os impactos de eventos como **ondas de calor** e **frio intenso**, que sobrecarregam sistemas de saúde e colocam a vida de grupos vulneráveis em risco.

---

### ⚙️ Funcionalidades Principais

| Funcionalidade | Descrição | Tecnologias Chave |
| :--- | :--- | :--- |
| **Monitoramento em Tempo Real** | Consulta APIs meteorológicas (como OpenWeatherMap, AccuWeather, etc.) para obter dados atualizados de temperatura, umidade, vento e pressão. | `requests` |
| **Cálculo de Índices de Risco** | Processa dados brutos para calcular índices relevantes, como **Sensação Térmica** e **Índice de Calor** (Heat Index), que refletem o estresse fisiológico no corpo humano. | `Python` (Lógica) |
| **Geração de Recomendações** | Algoritmo que, com base nos índices de risco e perfis de vulnerabilidade, gera recomendações de saúde específicas e práticas (ex: "Aumentar a hidratação", "Evitar exposição solar entre 10h e 16h"). | `Python` (Lógica) |
| **Interface Simples** | Permite a entrada de dados de localização (cidade/CEP) e apresenta as condições climáticas e as recomendações de forma clara e direta. | `Python` (CLI/Interface) |

---

### 💻 Tecnologias Utilizadas

O projeto foi construído com foco em simplicidade, eficiência e portabilidade:

| Tecnologia | Propósito |
| :--- | :--- |
| **Python** | Linguagem principal para lógica de negócios e processamento de dados. |
| **Requests** | Biblioteca essencial para realizar chamadas HTTP e consumir dados das APIs meteorológicas. |
| **Pandas** (Opcional) | Pode ser utilizado para manipulação e análise mais robusta de séries históricas de dados, caso o projeto evolua para incluir análise preditiva. |

---

### 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local.

#### 1. Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

#### 2. Clonar o Repositório

```bash
git clone https://github.com/gaherrera00/alerta-ambiental.git
cd alerta-ambiental
```

#### 3. Instalar Dependências

O projeto utiliza um conjunto mínimo de bibliotecas.

```bash
pip install -r requirements.txt
```

#### 4. Configurar Chaves de API

Para acessar os dados meteorológicos, você precisará de uma chave de API de um provedor de sua escolha (ex: OpenWeatherMap).

*   Crie um arquivo `.env` na raiz do projeto.
*   Adicione sua chave de API no formato:
    ```
    API_KEY="SUA_CHAVE_AQUI"
    ```
*   *Nota:* O projeto pode exigir a instalação de uma biblioteca para carregar variáveis de ambiente (ex: `python-dotenv`).

#### 5. Rodar a Aplicação

Execute o script principal:

```bash
python app.py
```

---

### 🤝 Contribuição

Contribuições são muito bem-vindas! Se você tem sugestões de melhoria, novas funcionalidades (como integração com mais APIs ou novos índices de risco) ou encontrou um bug, sinta-se à vontade para:

1.  Fazer um **Fork** do projeto.
2.  Criar uma **Branch** para sua feature (`git checkout -b feature/nova-funcionalidade`).
3.  Fazer o **Commit** de suas mudanças (`git commit -m 'feat: Adiciona nova funcionalidade X'`).
4.  Fazer o **Push** para a Branch (`git push origin feature/nova-funcionalidade`).
5.  Abrir um **Pull Request**.

---

### 📧 Contato

Gabriel Herrera Demarchi – [gabriel.h.demarchi@gmail.com](mailto:gabriel.h.demarchi@gmail.com)

Deploy - [https://alerta-ambiental-3r9phucbyvoenqpatxxsvm.streamlit.app/](https://alerta-ambiental-3r9phucbyvoenqpatxxsvm.streamlit.app/)

Link do Projeto: [https://github.com/seu-usuario/alerta-ambiental](https://github.com/seu-usuario/alerta-ambiental)
