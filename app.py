import streamlit as st
from openai import OpenAI
from prompts import complaint_prompt_template, directive_prompt_template, system_prompt

# Set up OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set up page config
st.set_page_config(page_title="ReclameAqui POC", layout="wide")
st.title("Prova de Conceito ReclameAqui")
st.write("Este aplicativo demonstra duas funcionalidades de LLM para aprimorar o processamento e reposta à reclamações para as empresas clientes do ReclameAqui.")

# Initialize OpenAI model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Function to stream GPT-4 response
def stream_gpt4_response(prompt):
    try:
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            stream=True,
            stream_options={"include_usage": True}
        )
        yield response

    except Exception as e:
        st.error(f"Ocorreu um erro ao comunicar com a API do OpenAI: {str(e)}")
        return None

# Text summarizer and information extraction feature
st.header("Processamento de Reclamações")
st.session_state['complaint'] = st.text_area("Digite a reclamação do cliente:", placeholder="Digite ou cole a reclamação do cliente aqui...")

if st.button("Resumir e Extrair Informações"):
    if st.session_state['complaint']:
        prompt = complaint_prompt_template.format(st.session_state['complaint'])
        st.write_stream(stream_gpt4_response(prompt))
    else:
        st.warning("Por favor, digite uma reclamação do cliente.")

# Text expansion feature
st.header("Geração de Resposta ao Consumidor")
st.session_state['directive'] = st.text_input("Digite a diretriz da empresa:", placeholder="Digite a diretriz da empresa aqui...")
if st.button("Gerar Resposta Detalhada"):
    if st.session_state['directive']:
        prompt = directive_prompt_template.format(st.session_state['complaint'], st.session_state['directive'])
        st.write_stream(stream_gpt4_response(prompt))
    else:
        st.warning("Por favor, digite uma diretriz da empresa.")
