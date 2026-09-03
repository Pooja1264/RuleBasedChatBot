import streamlit as st
import datetime
import random
import ast
import operator as op
import time

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="RuleBot | AI Chat Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS — polished, animated, glassy UI
# =========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #6366f1, #8b5cf6, #ec4899, #6366f1);
        background-size: 400% 400%;
        animation: gradientShift 18s ease infinite;
    }
    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main { padding-top: 0.5rem; }

    /* Glass container wrapping the whole app content */
    .block-container {
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(14px);
        border-radius: 28px;
        padding: 2rem 1.8rem !important;
        margin-top: 1rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    }

    /* Hero */
    .hero {
        padding: 34px 25px;
        border-radius: 22px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 60%, #ec4899 100%);
        color: white;
        text-align: center;
        margin-bottom: 22px;
        box-shadow: 0 14px 38px rgba(102, 70, 200, 0.35);
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 60%);
        animation: pulse 6s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.6; }
        50% { transform: scale(1.15); opacity: 1; }
    }
    .hero-icon {
        font-size: 54px;
        margin-bottom: 4px;
        animation: bounce 2.5s ease-in-out infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    .hero h1 {
        font-size: 44px;
        margin: 0;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .hero p {
        font-size: 16px;
        margin-top: 8px;
        opacity: 0.95;
        font-weight: 400;
    }
    .hero-badges {
        margin-top: 14px;
        display: flex;
        gap: 8px;
        justify-content: center;
        flex-wrap: wrap;
    }
    .hero-badge {
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.35);
        border-radius: 20px;
        padding: 5px 14px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Feature cards */
    .feature-card {
        padding: 20px 14px;
        border-radius: 18px;
        background: white;
        border: 1px solid #eef0f7;
        text-align: center;
        min-height: 118px;
        box-shadow: 0 6px 20px rgba(80,70,180,0.08);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(80,70,180,0.18);
    }
    .feature-icon { font-size: 30px; }
    .feature-title {
        font-size: 14.5px;
        font-weight: 700;
        margin-top: 7px;
        color: #312e81;
    }
    .feature-text {
        font-size: 12px;
        color: #6b7280;
        margin-top: 4px;
    }

    /* Info box */
    .info-box {
        padding: 18px 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #f5f3ff 0%, #eef2ff 100%);
        border: 1px solid #e0e7ff;
        margin-bottom: 18px;
        color: #3730a3;
        font-size: 14.5px;
        line-height: 1.6;
    }

    /* Divider styling */
    hr { border-color: #e5e7eb !important; }

    /* Chat bubbles */
    div[data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 4px 6px;
        margin-bottom: 6px;
        animation: fadeIn 0.35s ease;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Chat input */
    .stChatInput textarea, div[data-testid="stChatInput"] textarea {
        border-radius: 16px !important;
    }

    /* Sidebar — dark indigo theme with gold accents (fixes text/bg clash) */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1b4b 0%, #312e81 55%, #4c1d95 100%);
        border-right: 1px solid #3730a3;
    }
    section[data-testid="stSidebar"] * {
        color: #ede9fe !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #fbbf24 !important;
        font-weight: 800 !important;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li {
        color: #e0e7ff !important;
        font-size: 13.5px;
    }
    section[data-testid="stSidebar"] strong {
        color: #fde68a !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: #4c1d95 !important;
    }
    section[data-testid="stSidebar"] .stCode {
        border-radius: 10px;
    }
    section[data-testid="stSidebar"] .stCode code {
        background: #0f0d2b !important;
        color: #a5f3fc !important;
        border: 1px solid #4c1d95;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton button {
        border-radius: 14px !important;
        font-weight: 600 !important;
        border: none !important;
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(102, 70, 200, 0.35) !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 26px 0 10px;
        color: #9ca3af;
        font-size: 12.5px;
    }

    /* Section title */
    .section-title {
        font-size: 20px;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 10px;
        color: #312e81;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================
jokes = [
    "Why do programmers prefer Python? Because it's easy to read! 🐍",
    "Why did the computer get cold? It forgot to close Windows. 😂",
    "Debugging is like being a detective in a crime movie where you're also the criminal. 🕵️",
    "Why do programmers love dark mode? Because light attracts bugs! 🐛",
    "There are only 10 kinds of people: those who understand binary and those who don't. 😄"
]

quotes = [
    "Success comes from consistent practice. 🚀",
    "Never stop learning. 📚",
    "Every expert was once a beginner. 🌱",
    "Believe in yourself and keep coding! 💻",
    "Small progress every day leads to big results. ⭐",
    "Don't give up. Great things take time. 💪"
]

# =========================================================
# SAFE CALCULATOR
# =========================================================
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos
}

def safe_calculate(expression):
    """
    Safely evaluate basic mathematical expressions.
    Supports: +  -  *  /  %  **  ()
    """
    def calculate(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid number")
        elif isinstance(node, ast.BinOp):
            left = calculate(node.left)
            right = calculate(node.right)
            operator_type = type(node.op)
            if operator_type not in operators:
                raise ValueError("Operator not allowed")
            return operators[operator_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            value = calculate(node.operand)
            operator_type = type(node.op)
            if operator_type not in operators:
                raise ValueError("Operator not allowed")
            return operators[operator_type](value)
        else:
            raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return calculate(tree.body)

# =========================================================
# CHATBOT RESPONSE FUNCTION
# =========================================================
def chatbot_response(user_message):
    user = user_message.lower().strip()

    # GREETING
    if user in ["hi", "hello", "hey", "hii", "hiii",
                "good morning", "good afternoon", "good evening"]:
        return (
            "Hello! 👋 I'm **RuleBot**.\n\n"
            "I'm your friendly rule-based AI assistant. "
            "You can ask me about **AI, Python, date, time**, "
            "or try my **calculator, jokes and motivational quotes**! 🤖"
        )

    # HOW ARE YOU
    elif user in ["how are you", "how are you?"]:
        return "I'm doing great! 😄 Thanks for asking. How can I help you?"

    # NAME
    elif user in ["your name", "what is your name", "who are you"]:
        return (
            "My name is **RuleBot 🤖** — "
            "a rule-based AI chatbot built with **Python and Streamlit**."
        )

    # AI INFORMATION
    elif user in ["what is ai", "what is artificial intelligence", "define ai", "ai"]:
        return (
            "🧠 **Artificial Intelligence (AI)**\n\n"
            "AI is a branch of computer science that enables machines "
            "to perform tasks that normally require human intelligence.\n\n"
            "Examples include:\n"
            "• Speech recognition 🎤\n"
            "• Image recognition 📷\n"
            "• Recommendation systems 🎯\n"
            "• Chatbots 🤖\n"
            "• Self-driving technology 🚗"
        )

    # PYTHON INFORMATION
    elif user in ["what is python", "define python", "python"]:
        return (
            "🐍 **Python**\n\n"
            "Python is a high-level, interpreted programming language "
            "known for its simple and readable syntax.\n\n"
            "It is widely used for:\n"
            "• Artificial Intelligence 🤖\n"
            "• Machine Learning 🧠\n"
            "• Data Science 📊\n"
            "• Web Development 🌐\n"
            "• Automation ⚙️"
        )

    # DATE
    elif user in ["date", "today", "today's date", "what is today's date", "what is the date"]:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"📅 **Today's Date:** {current_date}"

    # TIME
    elif user in ["time", "current time", "what is the time", "what time is it"]:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"🕐 **Current Time:** {current_time}"

    # CALCULATOR
    elif user.startswith("calculate "):
        expression = user.replace("calculate ", "", 1).strip()
        try:
            result = safe_calculate(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return f"🧮 **Calculation Result**\n\n`{expression}` = **{result}**"
        except ZeroDivisionError:
            return "❌ Cannot divide by zero."
        except Exception:
            return (
                "❌ I couldn't calculate that.\n\n"
                "Try something like:\n"
                "`calculate 25+10*2`\n"
                "`calculate (100-20)/4`\n"
                "`calculate 5**2`"
            )

    # SHORT CALC
    elif user.startswith("calc "):
        expression = user.replace("calc ", "", 1).strip()
        try:
            result = safe_calculate(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return f"🧮 **Result:** {result}"
        except ZeroDivisionError:
            return "❌ Cannot divide by zero."
        except Exception:
            return "❌ Invalid calculation.\n\nExample: `calc 20+5*3`"

    # JOKE
    elif user in ["joke", "tell me a joke", "tell joke"]:
        return f"😂 **Here's a joke:**\n\n{random.choice(jokes)}"

    # QUOTE
    elif user in ["quote", "motivation", "motivational quote", "motivate me"]:
        return f"💡 **Motivational Quote:**\n\n{random.choice(quotes)}"

    # HELP
    elif user in ["help", "commands", "menu"]:
        return """
## 💡 RuleBot Commands
👋 **Greetings**
- `hello`
- `hi`
- `hey`

🧠 **Knowledge**
- `what is ai`
- `what is python`

📅 **Date & Time**
- `date`
- `time`

🧮 **Calculator**
- `calculate 25+10*2`
- `calculate (100-20)/4`
- `calc 5**2`

😂 **Fun**
- `joke`
- `quote`

🤖 **Other**
- `your name`
- `how are you`
- `help`

👋 **Exit**
- `bye`
- `exit`
- `quit`
"""

    # EXIT
    elif user in ["bye", "exit", "quit", "goodbye"]:
        return (
            "Goodbye! 👋\n\n"
            "Thanks for chatting with **RuleBot**. "
            "Keep learning and keep coding! 💻🚀"
        )

    # DEFAULT
    else:
        return (
            "🤔 I'm sorry, I don't understand that yet.\n\n"
            "Type **help** to see all the commands I can handle."
        )

# =========================================================
# HERO SECTION
# =========================================================
st.markdown("""
<div class="hero">
    <div class="hero-icon">🤖</div>
    <h1>RuleBot</h1>
    <p>Your Friendly Rule-Based AI Chat Assistant</p>
    <div class="hero-badges">
        <span class="hero-badge">🧠 AI & Python</span>
        <span class="hero-badge">🧮 Calculator</span>
        <span class="hero-badge">😂 Jokes</span>
        <span class="hero-badge">💡 Quotes</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# INTRO
# =========================================================
st.markdown("""
<div class="info-box">
<b>👋 Welcome to RuleBot!</b><br><br>
I'm a simple rule-based chatbot built using <b>Python + Streamlit</b>.
Ask me about AI or Python, check the date and time,
perform calculations, or have some fun with jokes and quotes! 🚀
</div>
""", unsafe_allow_html=True)

# =========================================================
# FEATURE CARDS
# =========================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">AI Knowledge</div>
        <div class="feature-text">Learn AI & Python basics</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧮</div>
        <div class="feature-title">Smart Calculator</div>
        <div class="feature-text">Perform quick calculations</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Fun Commands</div>
        <div class="feature-text">Jokes, quotes & more</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-title'>💬 Chat with RuleBot</div>", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm **RuleBot**.\n\n"
                "Type **help** to see everything I can do."
            )
        }
    ]

# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🧑‍💻"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# =========================================================
# CHAT INPUT
# =========================================================
user_input = st.chat_input("💬 Ask RuleBot something...")

# =========================================================
# PROCESS USER INPUT
# =========================================================
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("RuleBot is thinking..."):
            time.sleep(0.35)  # tiny delay for a natural "typing" feel
        response = chatbot_response(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("## 🤖 RuleBot")
    st.markdown(
        """
        ### About
        RuleBot is a Python-based rule-driven chatbot
        designed to demonstrate:
        - 💬 Conversational UI
        - 🧠 Rule-based decision making
        - 🧮 Calculator functionality
        - 📅 Date & time handling
        - 😂 Random responses
        """
    )
    st.divider()
    st.subheader("⚡ Try These")
    commands = [
        "hello", "what is ai", "what is python", "date", "time",
        "calculate 25+10*2", "joke", "quote", "help", "bye"
    ]
    for command in commands:
        st.code(command)

    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋 I'm **RuleBot**.\n\n"
                    "Conversation cleared! Type **help** to see my commands."
                )
            }
        ]
        st.rerun()

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    Built with ❤️ using Python + Streamlit
    <br>
    RuleBot • Rule-Based AI Chat Assistant
</div>
""", unsafe_allow_html=True)
