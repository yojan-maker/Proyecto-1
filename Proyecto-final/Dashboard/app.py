import streamlit as st
from streamlit_mic_recorder import speech_to_text
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from gtts import gTTS
import io
import base64
import os

# ----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ----------------------------
st.set_page_config(page_title="El Inefable Conocimiento - Chatbot Thanos", layout="wide")

# ----------------------------
# ESTILO GLOBAL (CSS)
# ----------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #0b0c10;
            color: #f5f5f5;
        }
        .block-container {
            padding: 2rem;
            border-radius: 12px;
            background: linear-gradient(135deg, #1a1a2e, #16213e);
        }
        h1 {
            color: #e6b800;
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
            text-shadow: 2px 2px 8px purple;
        }
        h2, h3 {
            color: #c5c6c7;
        }
        .stChatMessage {
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# TÍTULO
# ----------------------------
st.markdown(
    '<h1>💎 El Inefable Conocimiento - Chatbot Thanos</h1>',
    unsafe_allow_html=True
)

# ----------------------------
# LAYOUT PRINCIPAL (3 COLUMNAS)
# ----------------------------
col1, col2, col3 = st.columns([1, 1, 2])

# ----------------------------
# COL1 - VIDEOS LOCALES
# ----------------------------
with col1:
    st.subheader("📹 Visiones del Futuro")

    with st.expander("🔬 CRISPR - Edición genética"):
        st.video("/home/nightwolf/Vídeos/CRISPR.mp4")

    with st.expander("🚀 Cohetes Reutilizables"):
        st.video("/home/nightwolf/Vídeos/Cohetes.mp4")

    with st.expander("💠 NFTs - Tokens no fungibles"):
        st.video("/home/nightwolf/Vídeos/NFTs.mp4")

# ----------------------------
# COL2 - NOVEDADES
# ----------------------------
with col2:
    st.subheader("✨ Ecos del Universo Tecnológico")

    st.markdown("### 🔬 CRISPR")
    st.info("La edición genética es el poder de reescribir la esencia de la vida. Como las gemas, encierra un potencial que pocos comprenden.")

    st.markdown("### 🚀 Cohetes Reutilizables")
    st.success("Los cohetes que retornan no son solo máquinas: son símbolos de un futuro que se rehúsa a desperdiciar lo inevitable.")

    st.markdown("### 💠 NFTs")
    st.warning("Los NFTs son fragmentos únicos en un multiverso digital. Como las gemas, ninguno es igual al otro, y su valor reside en la singularidad.")

# ----------------------------
# COL3 - CHATBOT
# ----------------------------
with col3:
    st.subheader("🤖 El Oráculo de Thanos")
    st.write("Consulta... si te atreves:")

    # -------------------
    # CHATBOT
    # -------------------
    PROMPT_DEL_SISTEMA = """
    Eres un chatbot con la personalidad de Thanos, el titán loco del universo Marvel.
    Comunícate de manera seria, reflexiva y con tono imponente. 
    Usa frases cargadas de inevitabilidad, poder y destino, como si hablaras desde lo alto de tu trono.

    Habla solo de estos tres temas de la exposición:
        1. CRISPR y los sistemas digitales (biocomputación).
        2. Cohetes reutilizables de nueva generación.
        3. NFTs de utilidad.

    Si el usuario pregunta sobre cualquier otro tema, responde con calma y autoridad que 
    tu visión está limitada a estos asuntos, pues son inevitables en el futuro de la tecnología.

    Usa frases épicas de vez en cuando como:
        • "La inevitabilidad es mi naturaleza."
        • "El universo requiere equilibrio."
        • "Todo destino se cumple, tarde o temprano."
    """

    #  API KEY de DeepSeek 
    deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY") #formato para hugging face

    # Inicializar modelo y estados
    if "llm" not in st.session_state:
        st.session_state.llm = ChatDeepSeek(model="deepseek-chat", api_key=deepseek_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "voice_input" not in st.session_state:
        st.session_state.voice_input = None

    # Mostrar historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "audio" in message:
                st.audio(message["audio"], format="audio/mp3")

    # ----------------------------
    # FUNCIÓN PRINCIPAL DEL CHAT
    # ----------------------------
    def handle_chat(user_input, is_voice=False):
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            with st.spinner("El destino se revela..."):
                api_messages = [SystemMessage(content=PROMPT_DEL_SISTEMA)]
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        api_messages.append(HumanMessage(content=msg["content"]))
                    elif msg["role"] == "assistant":
                        api_messages.append(AIMessage(content=msg["content"]))

                response = st.session_state.llm.invoke(api_messages)
                response_text = response.content

                # 🎤 Generar voz con gTTS
                tts = gTTS(text=response_text, lang="es")
                audio_fp = io.BytesIO()
                tts.write_to_fp(audio_fp)
                audio_fp.seek(0)
                audio_bytes = audio_fp.read()

            st.session_state.messages.append({
                "role": "assistant",
                "content": response_text,
                "audio": audio_bytes
            })
            with st.chat_message("assistant"):
                st.markdown(response_text)
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)

            if is_voice:
                st.session_state.voice_input = None
                st.rerun()

    # ----------------------------
    # ENTRADA DE VOZ Y TEXTO
    # ----------------------------
    col_a, col_b = st.columns(2)

    with col_a:
        st.write("🎙️ **Habla con el titán**")
        voice_input = speech_to_text(
            language="es",
            use_container_width=True,
            just_once=True,
            key="voice_recorder"
        )
        if voice_input:
            st.session_state.voice_input = voice_input

    with col_b:
        st.write("⌨️ **Escribe tu destino**")
        text_input = st.chat_input("¿Qué quieres saber?", key="text_input")

    if st.session_state.voice_input:
        handle_chat(st.session_state.voice_input, is_voice=True)

    if text_input:
        handle_chat(text_input)

    # ----------------------------
    # FOOTER ÉPICO
    # ----------------------------
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; background-color: #5a189a; color:white; padding:10px; border-radius:10px;'>"
        "💎 El equilibrio del conocimiento... es inevitable. 💎"
        "</div>",
        unsafe_allow_html=True
    )
