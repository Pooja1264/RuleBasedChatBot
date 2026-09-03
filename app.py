import streamlit as st
import datetime
import random
import ast
import operator as op


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="RuleBot | AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    .main {
        padding-top: 1rem;
    }

    /* Hero */
    .hero {
        padding: 30px 25px;
        border-radius: 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 12px 35px rgba(80, 70, 180, 0.25);
    }

    .hero-icon {
        font-size: 50px;
        margin-bottom: 5px;
    }

    .hero h1 {
        font-size: 42px;
        margin: 0;
        font-weight: 700;
    }

    .hero p {
        font-size: 17px;
        margin-top: 8px;
        opacity: 0.95;
    }

    /* Feature cards */
    .feature-card {
        padding: 20px 15px;
        border-radius: 18px;
        background: white;
        border: 1px solid #e5e7eb;
        text-align: center;
        min-height: 115px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    }

    .feature-icon {
        font-size: 28px;
    }

    .feature-title {
        font-size: 15px;
        font-weight: 700;
        margin-top: 7px;
    }

    .feature-text {
        font-size: 12px;
        color: #6b7280;
        margin-top: 5px;
    }

    /* Section heading */
    .section-title {
        font-size: 21px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Info box */
    .info-box {
        padding: 16px;
        border-radius: 15px;
        background: white;
        border: 1px solid #e5e7eb;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px 0 15px;
        color: #6b7280;
        font-size: 13px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #f8f9ff;
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
    Supports:
    +  -  *  /  %  **  ()
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

    # -----------------------------------------------------
    # GREETING
    # -----------------------------------------------------

    if user in [
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return (
            "Hello! 👋 I'm **RuleBot**.\n\n"
            "I'm your friendly rule-based AI assistant. "
            "You can ask me about **AI, Python, date, time**, "
            "or try my **calculator, jokes and motivational quotes**! 🤖"
        )

    # -----------------------------------------------------
    # HOW ARE YOU
    # -----------------------------------------------------

    elif user in [
        "how are you",
        "how are you?"
    ]:
        return "I'm doing great! 😄 Thanks for asking. How can I help you?"

    # -----------------------------------------------------
    # NAME
    # -----------------------------------------------------

    elif user in [
        "your name",
        "what is your name",
        "who are you"
    ]:
        return (
            "My name is **RuleBot 🤖** — "
            "a rule-based AI chatbot built with **Python and Streamlit**."
        )

    # -----------------------------------------------------
    # AI INFORMATION
    # -----------------------------------------------------

    elif user in [
        "what is ai",
        "what is artificial intelligence",
        "define ai",
        "ai"
    ]:
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

    # -----------------------------------------------------
    # PYTHON INFORMATION
    # -----------------------------------------------------

    elif user in [
        "what is python",
        "define python",
        "python"
    ]:
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

    # -----------------------------------------------------
    # DATE
    # -----------------------------------------------------

    elif user in [
        "date",
        "today",
        "today's date",
        "what is today's date",
        "what is the date"
    ]:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")

        return f"📅 **Today's Date:** {current_date}"

    # -----------------------------------------------------
    # TIME
    # -----------------------------------------------------

    elif user in [
        "time",
        "current time",
        "what is the time",
        "what time is it"
    ]:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")

        return f"🕐 **Current Time:** {current_time}"

    # -----------------------------------------------------
    # CALCULATOR
    # -----------------------------------------------------

    elif user.startswith("calculate "):

        expression = user.replace("calculate ", "", 1).strip()

        try:

            result = safe_calculate(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            return (
                f"🧮 **Calculation Result**\n\n"
                f"`{expression}` = **{result}**"
            )

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

    # -----------------------------------------------------
    # ALSO SUPPORT SIMPLE CALCULATION
    # -----------------------------------------------------

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
            return (
                "❌ Invalid calculation.\n\n"
                "Example: `calc 20+5*3`"
            )

    # -----------------------------------------------------
    # JOKE
    # -----------------------------------------------------

    elif user in [
        "joke",
        "tell me a joke",
        "tell joke"
    ]:
        return f"😂 **Here's a joke:**\n\n{random.choice(jokes)}"

    # -----------------------------------------------------
    # QUOTE
    # -----------------------------------------------------

    elif user in [
        "quote",
        "motivation",
        "motivational quote",
        "motivate me"
    ]:
        return f"💡 **Motivational Quote:**\n\n{random.choice(quotes)}"

    # -----------------------------------------------------
    # HELP
    # -----------------------------------------------------

    elif user in [
        "help",
        "commands",
        "menu"
    ]:
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

    # -----------------------------------------------------
    # EXIT
    # -----------------------------------------------------

    elif user in [
        "bye",
        "exit",
        "quit",
        "goodbye"
    ]:
        return (
            "Goodbye! 👋\n\n"
            "Thanks for chatting with **RuleBot**. "
            "Keep learning and keep coding! 💻🚀"
        )

    # -----------------------------------------------------
    # DEFAULT RESPONSE
    # -----------------------------------------------------

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

    <p>
        Your Friendly Rule-Based AI Chat Assistant
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRO
# =========================================================

st.markdown("""
<div class="info-box">

<b>👋 Welcome to RuleBot!</b>

<br><br>

I'm a simple rule-based chatbot built using
<b>Python + Streamlit</b>.

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
        <div class="feature-text">
            Learn AI & Python basics
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧮</div>
        <div class="feature-title">Smart Calculator</div>
        <div class="feature-text">
            Perform quick calculations
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Fun Commands</div>
        <div class="feature-text">
            Jokes, quotes & more
        </div>
    </div>
    """, unsafe_allow_html=True)


st.divider()


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

    if message["role"] == "assistant":
        avatar = "🤖"
    else:
        avatar = "🧑‍💻"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):
        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "💬 Ask RuleBot something..."
)


# =========================================================
# PROCESS USER INPUT
# =========================================================

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message(
        "user",
        avatar="🧑‍💻"
    ):
        st.markdown(user_input)

    # Generate response
    response = chatbot_response(user_input)

    # Add assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Display assistant response
    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):
        st.markdown(response)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤖 RuleBot")

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
        "hello",
        "what is ai",
        "what is python",
        "date",
        "time",
        "calculate 25+10*2",
        "joke",
        "quote",
        "help",
        "bye"
    ]

    for command in commands:
        st.code(command)

    st.divider()

    # Clear chat
    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋 I'm **RuleBot**.\n\n"
                    "Conversation cleared! "
                    "Type **help** to see my commands."
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
