import streamlit as st
import datetime
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="RuleBot | AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .hero {
        padding: 28px;
        border-radius: 22px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.95;
    }

    .feature-card {
        padding: 18px;
        border-radius: 16px;
        background: rgba(128,128,128,0.08);
        border: 1px solid rgba(128,128,128,0.18);
        margin-bottom: 10px;
    }

    .footer {
        text-align: center;
        padding: 25px 0 10px;
        opacity: 0.65;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- DATA ----------------
jokes = [
    "Why do programmers prefer Python? Because it's easy to read! 🐍",
    "Why did the computer get cold? It forgot to close Windows. 😂",
    "Debugging: Being the detective in a crime movie where you're also the criminal. 🕵️"
]

quotes = [
    "Success comes from consistent practice. 🚀",
    "Never stop learning. 📚",
    "Every expert was once a beginner. 🌱",
    "Believe in yourself and keep coding! 💻"
]


# ---------------- CHATBOT LOGIC ----------------
def chatbot_response(user):
    user = user.lower().strip()

    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello! 👋 I'm RuleBot. How can I help you today?"

    elif user == "how are you":
        return "I'm doing great! 😄 Thanks for asking."

    elif user == "your name":
        return "My name is RuleBot 🤖 — a rule-based AI chatbot."

    elif user == "what is ai":
        return (
            "AI (Artificial Intelligence) enables machines to perform "
            "tasks that normally require human intelligence."
        )

    elif user == "what is python":
        return (
            "Python is a powerful programming language used in "
            "AI, Data Science, Web Development and Automation. 🐍"
        )

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"🕐 Current Time: **{current_time}**"

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"📅 Today's Date: **{current_date}**"

    elif user == "joke":
        return random.choice(jokes)

    elif user == "quote":
        return random.choice(quotes)

    elif user == "help":
        return """
### 💡 Available Commands

👋 **hello**  
😊 **how are you**  
🤖 **your name**  
🧠 **what is ai**  
🐍 **what is python**  
🕐 **time**  
📅 **date**  
😂 **joke**  
💭 **quote**  
❓ **help**  
👋 **bye**
"""

    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Thanks for chatting with RuleBot."

    else:
        return (
            "I'm sorry, I don't understand that yet. 🤔\n\n"
            "Type **help** to see what I can do."
        )


# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <h1>🤖 RuleBot</h1>
    <p>Your Friendly Rule-Based AI Chat Assistant</p>
</div>
""", unsafe_allow_html=True)

st.write(
    "Welcome! I'm RuleBot — a simple AI chatbot built with "
    "**Python and Streamlit**. Try the commands below or ask me something!"
)

# ---------------- FEATURES ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="feature-card"><b>🧠 AI Knowledge</b><br>'
        'Learn basic AI & Python concepts.</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="feature-card"><b>⚡ Quick Responses</b><br>'
        'Get instant rule-based answers.</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="feature-card"><b>🎯 Fun Commands</b><br>'
        'Try jokes, quotes, date & time.</div>',
        unsafe_allow_html=True
    )

st.divider()


# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm RuleBot. Type **help** to see what I can do."
        }
    ]


# Display messages
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🧑‍💻"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("💬 Type your message here...")

if user_input:

    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # Bot response
    response = chatbot_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🤖 RuleBot")

    st.markdown(
        "### About\n"
        "RuleBot is a Python-based rule-driven chatbot "
        "designed to demonstrate conversational UI and "
        "basic decision-making logic."
    )

    st.divider()

    st.subheader("⚡ Try These")

    commands = [
        "hello",
        "what is ai",
        "what is python",
        "joke",
        "quote",
        "time",
        "date",
        "help"
    ]

    for command in commands:
        st.code(command)

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Built with ❤️ using Python + Streamlit
</div>
""", unsafe_allow_html=True)
