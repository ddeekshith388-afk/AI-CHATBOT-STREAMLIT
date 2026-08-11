import streamlit as st
from datetime import datetime


# =================================================
# 1. PAGE CONFIGURATION
# =================================================

st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# =================================================
# 2. CUSTOM DESIGN
# =================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f5f7fa,
        #e4ecf7
    );
}

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 16px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# =================================================
# 3. SIDEBAR
# =================================================

with st.sidebar:

    st.header("⚙️ Settings")

    name = st.text_input(
        "🤖 Assistant Name",
        "My AI Assistant"
    )

    show_time = st.checkbox(
        "🕐 Show Time",
        value=True
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# =================================================
# 4. HEADER
# =================================================

st.markdown(
    f'<div class="main-title">🤖 {name}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ Your smart conversational assistant</div>',
    unsafe_allow_html=True
)


# =================================================
# 5. CREATE CHAT HISTORY
# =================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": "👋 Hello! How can I help you today?",
            "time": datetime.now().strftime("%I:%M %p")
        }

    ]


# =================================================
# 6. DISPLAY CHAT HISTORY
# =================================================

for message in st.session_state.messages:

    if message["role"] == "assistant":
        avatar = "🤖"
    else:
        avatar = "👤"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.write(message["content"])

        if show_time:
            st.caption(
                "🕐 " + message["time"]
            )


# =================================================
# 7. USER INPUT
# =================================================

user_message = st.chat_input(
    "💬 Type your message..."
)


# =================================================
# 8. PROCESS USER MESSAGE
# =================================================

if user_message:

    current_time = datetime.now().strftime(
        "%I:%M %p"
    )

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
            "time": current_time
        }
    )

    # Temporary AI response
    bot_response = (
        f"🤖 You said: {user_message}"
    )

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response,
            "time": current_time
        }
    )

    # Refresh the page
    st.rerun()