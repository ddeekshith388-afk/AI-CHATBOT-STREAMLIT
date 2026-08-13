import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from google import genai


# ============================================================
# 1. LOAD API KEYS
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ============================================================
# 2. PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ============================================================
# 3. WHITE UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #ffffff;
    color: #111111;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 15px;
    color: #777777;
    margin-bottom: 30px;
}

section[data-testid="stSidebar"] {
    background-color: #f8f8f8;
}

.stButton button {
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 4. HEADER
# ============================================================

st.markdown(
    '<div class="title">🤖 AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your AI model from Settings</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. SETTINGS
# ============================================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    # --------------------------------------------------------
    # MODEL
    # --------------------------------------------------------

    st.subheader("🤖 Model")

    model_choice = st.selectbox(
        "Choose model",
        [
            "OpenAI - GPT-5 Mini",
            "OpenAI - GPT-4.1 Mini",
            "Gemini - Gemini Flash",
            "Gemini - Gemini Pro",
            "Normal - Basic Assistant"
        ]
    )

    # --------------------------------------------------------
    # TEMPERATURE
    # --------------------------------------------------------

    st.subheader("🌡️ Temperature")

    temperature = st.slider(
        "Response creativity",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1
    )

    if temperature < 0.5:

        st.caption("🎯 More focused")

    elif temperature < 1.2:

        st.caption("⚖️ Balanced")

    else:

        st.caption("✨ More creative")

    st.markdown("---")

    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# 6. INITIALIZE CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# 7. DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# 8. USER INPUT
# ============================================================

user_message = st.chat_input(
    "Type your message..."
)


# ============================================================
# 9. AI RESPONSE
# ============================================================

if user_message:

    # --------------------------------------------------------
    # SHOW USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):

        st.markdown(user_message)


    # --------------------------------------------------------
    # ASSISTANT RESPONSE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        try:

            # =================================================
            # OPENAI
            # =================================================

            if model_choice == "OpenAI - GPT-5 Mini":

                if not OPENAI_API_KEY:

                    st.error(
                        "OpenAI API key is missing."
                    )

                else:

                    client = OpenAI(
                        api_key=OPENAI_API_KEY
                    )

                    response = client.responses.create(
                        model="gpt-5-mini",
                        input=user_message
                    )

                    answer = response.output_text

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )


            # =================================================
            # OPENAI GPT-4.1 MINI
            # =================================================

            elif model_choice == "OpenAI - GPT-4.1 Mini":

                if not OPENAI_API_KEY:

                    st.error(
                        "OpenAI API key is missing."
                    )

                else:

                    client = OpenAI(
                        api_key=OPENAI_API_KEY
                    )

                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        input=user_message
                    )

                    answer = response.output_text

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )


            # =================================================
            # GEMINI FLASH
            # =================================================

            elif model_choice == "Gemini - Gemini Flash":

                if not GEMINI_API_KEY:

                    st.error(
                        "Gemini API key is missing."
                    )

                else:

                    client = genai.Client(
                        api_key=GEMINI_API_KEY
                    )

                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=user_message
                    )

                    answer = response.text

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )


            # =================================================
            # GEMINI PRO
            # =================================================

            elif model_choice == "Gemini - Gemini Pro":

                if not GEMINI_API_KEY:

                    st.error(
                        "Gemini API key is missing."
                    )

                else:

                    client = genai.Client(
                        api_key=GEMINI_API_KEY
                    )

                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=user_message
                    )

                    answer = response.text

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )


            # =================================================
            # NORMAL ASSISTANT
            # =================================================

            elif model_choice == "Normal - Basic Assistant":

                answer = (
                    "You selected Normal Assistant.\n\n"
                    "This mode does not use an API key. "
                    "It is a basic local response mode."
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )


# ============================================================
# 10. CURRENT SETTINGS
# ============================================================

st.caption(
    f"Model: {model_choice}  •  Temperature: {temperature}"
)