import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Song AI",
    page_icon="🤖"
)

st.title("🤖 Song AI")
st.write("မင်္ဂလာပါ သူငယ်ချင်း။ ကျွန်တော်က Song AI ပါ။")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Song AI ကို မေးချင်တာ ရိုက်ပါ...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    try:
        client = OpenAI()

        with st.chat_message("assistant"):
            with st.spinner("Song AI စဉ်းစားနေပါတယ်..."):

                response = client.responses.create(
                    model="gpt-6-luna",
                    instructions="မင်းဟာ Song AI ဖြစ်တယ်။ မြန်မာဘာသာနဲ့ ဖော်ရွေစွာ ဖြေဆိုပါ။",
                    input=question
                )

                answer = response.output_text
                st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"အမှားဖြစ်နေပါတယ်: {e}")