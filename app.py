import streamlit as st
import datetime
import random

st.set_page_config(
    page_title="RuleBot - AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Chatbot Data
# -----------------------------

jokes = [
    "Why do programmers prefer Python? Because it's easy to read!",
    "Why did the computer get cold? It forgot to close Windows.",
    "Debugging: Being the detective in a crime movie where you're also the criminal."
]

quotes = [
    "Success comes from consistent practice.",
    "Never stop learning.",
    "Every expert was once a beginner.",
    "Believe in yourself and keep coding!"
]


# -----------------------------
# Rule-Based Chatbot Function
# -----------------------------

def chatbot_response(user):
    user = user.lower().strip()

    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello! 😊 How can I help you today?"

    elif user == "how are you":
        return "I'm doing great! Thanks for asking. 😄"

    elif user == "your name":
        return "My name is RuleBot 🤖."

    elif user == "what is ai":
        return "AI (Artificial Intelligence) enables machines to perform tasks that normally require human intelligence."

    elif user == "what is python":
        return "Python is a powerful programming language used in AI, Data Science, Web Development, and Automation."

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"Current Time: {current_time}"

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's Date: {current_date}"

    elif user == "joke":
        return random.choice(jokes)

    elif user == "quote":
        return random.choice(quotes)

    elif user == "help":
        return """
**Available Commands:**

- hi / hello / hey
- how are you
- your name
- what is ai
- what is python
- date
- time
- joke
- quote
- calculator
- help
- bye
"""

    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I don't understand that. Type **help** to see available commands."


# -----------------------------
# Page UI
# -----------------------------

st.title("🤖 RuleBot")
st.subheader("Rule-Based AI Chatbot")

st.write(
    "Welcome! I'm RuleBot, a simple rule-based chatbot. "
    "Ask me something or try one of the commands below."
)

# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User Input
# -----------------------------

user_input = st.chat_input("Type your message...")

if user_input:

    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    response = chatbot_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("💡 Commands")

    st.write("""
    Try these commands:

    👋 `hello`

    😊 `how are you`

    🤖 `your name`

    🧠 `what is ai`

    🐍 `what is python`

    🕐 `time`

    📅 `date`

    😂 `joke`

    💭 `quote`

    ❓ `help`

    👋 `bye`
    """)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
