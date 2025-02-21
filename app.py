import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🧠", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stTextArea {
            border-radius: 5px;
            border: 1px solid #ddd;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Growth Mindset Project")
st.header("🧠 Welcome to the Growth Mindset Challenge!")
st.write("This interactive web app is designed to inspire and encourage a growth mindset. **Explore, learn, and embrace challenges as opportunities to grow.** 💡")

st.markdown("---")  

st.subheader("🌱 **Quote of the Day**")
st.success("💬 *Every challenge is an opportunity to grow. Embrace the struggle, learn from mistakes, and keep pushing forward!* 🌟")

st.markdown("---")

st.subheader("🎯 **What's Your Challenge for Today?**")
user_input = st.text_input("Enter your challenge for today ✍️")

if user_input:
    st.success(f"🌟 **Your challenge for today is:** {user_input}\n\nBelieve in your potential—every step you take brings you closer to success! 🚀")
else:
    st.warning("⚡ Enter your challenge for today to stay motivated!")

st.markdown("---")  
st.subheader("🔄 **Reflect On Your Learning**")
reflection = st.text_area("What did you learn today? 📝")

if reflection:
    st.success(f"💪 **Great Reflection:** {reflection}")
else:
    st.info("💡 *Your past mistakes are not failures—they are lessons that shape your future success. Keep learning and growing!* 🔥")

st.markdown("---")  

st.subheader("🏆 **Celebrate Your Achievements**")
achievement = st.text_area("What did you achieve today? 🎉")

if achievement:
    st.balloons() 
    st.success(f"🎊 **Congratulations! You achieved:** {achievement}")
else:
    st.info("👏 *Celebrate your progress, no matter how small. Every step you take is a step closer to your goals!*")

st.markdown("---")  

st.write("💡 **Believe in yourself, and you're already halfway there.** 🚀 Trust your journey, embrace the challenges, and keep growing!")


st.write("©️ 2024 **Growth Mindset Challenge**. All Rights Reserved. | Created by **Muhammad Usaid Khan**")
