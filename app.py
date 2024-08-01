import streamlit as st
from openai import AsyncOpenAI
import asyncio
from prompts import complaint_prompt_template, directive_prompt_template, system_prompt

# Set up OpenAI client
try:
    client = AsyncOpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    client = AsyncOpenAI()

# Set up page config
st.set_page_config(page_title="POC ReclameAqui", layout="wide", page_icon="imgs/ra_logo.png")
st.image("imgs/ra_logo_big.png", width=300)

col1, col2 = st.columns(2)
col1.markdown("""
##### ⚙️ **Funcionalidades**
Esta aplicação demonstra duas funcionalidades utilizando modelos de linguagem:\n
1. **Processamento de reclamações**: Reestrutura reclamações de clientes em um formato organizado.
2. **Geração de respostas ao consumidor**: Gera respostas detalhadas com base nas diretrizes da empresa.
""")
col2.markdown("""
##### 📝 **Instruções**
1. Insira a reclamação do cliente no campo de texto e clique em "Resumir e Extrair Informações".
2. Insira a diretriz da empresa no campo de texto e clique em "Gerar Resposta Detalhada".
3. A resposta gerada será exibida na caixa de texto abaixo do botão correspondente.
""")

# Initialize OpenAI model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = st.secrets["MODEL"]

# Initialize placeholders
if "complaint_placeholder" not in st.session_state:
    st.session_state["complaint_placeholder"] = ""
if "response_placeholder" not in st.session_state:
    st.session_state["response_placeholder"] = ""

# Function to stream GPT-4 response
async def stream_gpt4_response(prompt, placeholder_key):
    try:
        stream = await client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            stream=True
        )
        streamed_text = ""
        placeholder = st.empty()  # Create a placeholder for the info box
        async for chunk in stream:
            chunk_content = chunk.choices[0].delta.content
            if chunk_content is not None:
                streamed_text += chunk_content
                st.session_state[placeholder_key] = streamed_text
                placeholder.info(streamed_text, icon="🤖")  # Update the placeholder content
    except Exception as e:
        st.error(f"Ocorreu um erro ao comunicar com a API do OpenAI: {str(e)}")

# Text summarizer and information extraction feature
st.header("1. Processamento de Reclamações")
complaint = st.text_area("Digite a reclamação do cliente:", placeholder="Digite ou cole a reclamação do cliente aqui...")

if st.button("Resumir e Extrair Informações"):
    if complaint:
        prompt = complaint_prompt_template.format(complaint)
        asyncio.run(stream_gpt4_response(prompt, "complaint_placeholder"))
    else:
        st.warning("Por favor, digite uma reclamação do cliente.")
else:
    if len(st.session_state["complaint_placeholder"]) > 0:
        st.info(st.session_state["complaint_placeholder"], icon="🤖")

# Text expansion feature
st.header("2. Geração de Resposta ao Consumidor")
directive = st.text_input("Digite a diretriz da empresa:", placeholder="Digite a diretriz da empresa aqui...")

if st.button("Gerar Resposta Detalhada"):
    if not complaint:
        st.warning("Por favor, digite uma reclamação do cliente.")
    else:
        if directive:
            prompt = directive_prompt_template.format(complaint, directive)
            asyncio.run(stream_gpt4_response(prompt, "response_placeholder"))
        else:
            st.warning("Por favor, digite uma diretriz da empresa.")
else:
    if len(st.session_state["response_placeholder"]) > 0:
        st.info(st.session_state["response_placeholder"], icon="🤖")
