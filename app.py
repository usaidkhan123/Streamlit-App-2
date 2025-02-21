import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🧠")

st.title("🚀 Growth Mindset Project")
st.header("🧠 Welcome to the Growth Mindset Challenge!")
st.write("This interactive web app is designed to inspire and encourage a growth mindset. **Explore, learn, and embrace challenges as opportunities to grow.** 💡")

st.divider()

st.subheader("🌟 What is a Growth Mindset?")
st.write("A growth mindset means believing that **your abilities can develop** through dedication and hard work. 💡")
st.write("✅ Embrace challenges instead of avoiding them.")  
st.write("✅ Learn from mistakes and feedback.")  
st.write("✅ Effort leads to mastery—keep practicing!")  
st.write("✅ View failure as a learning experience.")  

st.divider()

st.subheader("🌱 Quote of the Day")
st.success("💬 *Every challenge is an opportunity to grow. Embrace the struggle, learn from mistakes, and keep pushing forward!* 🌟")

st.divider()

st.subheader("🎯 What’s Your Challenge for Today?")
user_input = st.text_input("Enter your challenge for today ✍️")

if user_input:
    st.success(f"🌟 **Your challenge for today:** {user_input}\n\n💪 Believe in your potential—every step you take brings you closer to success! 🚀")
else:
    st.warning("⚡ Don't hold back! Enter your challenge for today to stay motivated!")

st.divider()

st.subheader("🔄 Reflect On Your Learning")
st.write("💭 *Thinking about what you've learned helps reinforce new knowledge and skills!*")
reflection = st.text_area("What did you learn today? 📝")

if reflection:
    st.success(f"💪 **Great Reflection:** {reflection}")
else:
    st.info("💡 *Mistakes aren’t failures—they're lessons guiding your success. Keep learning and growing!* 🔥")

st.divider()

st.subheader("🏆 Celebrate Your Achievements")
st.write("🎉 *Recognizing and celebrating progress keeps you motivated!*")
achievement = st.text_area("What did you achieve today? 🎉")

if achievement:
    st.balloons()  
    st.success(f"🎊 **Congratulations! You achieved:** {achievement}")
else:
    st.info("👏 *Every small win counts! Keep celebrating your progress!*")

st.divider()

st.subheader("🚀 Take Action & Stay Motivated")
st.write("🔹 **Set small goals** and challenge yourself every day.")  
st.write("🔹 **Seek feedback** and use it to improve.")  
st.write("🔹 **Stay consistent**—growth happens over time!")  

if st.button("🔥 Stay Motivated!"):
    st.write("🌟 Keep pushing forward and never stop believing in yourself!")

st.divider()

st.subheader("📌 Tips for Building a Strong Growth Mindset")
st.write("🔸 View obstacles as learning opportunities.")  
st.write("🔸 Replace ‘I can’t’ with ‘I’ll try and improve.’")  
st.write("🔸 Celebrate progress, not just results.")  

st.divider()

st.subheader("🌍 Join the Growth Mindset Community!")
st.write("💬 *Connect with like-minded people and share your journey!*")  
st.write("📢 **Share your achievements in your WhatsApp group!**")  

st.divider()

st.subheader("💡 Believe in Yourself!")
st.write("**Every step you take brings you closer to success. Keep pushing forward, keep learning, and never stop growing! 🚀**")

st.write("©️ 2024 **Growth Mindset Challenge** | Created by **Muhammad Usaid Khan**")
