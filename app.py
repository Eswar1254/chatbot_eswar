# app.py
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

def display_chat_history(messages):
    for message in messages:
        st.write(f"{message['role'].capitalize()}: {message['content']}")

def get_assistant_response(messages):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r['choices'][0]['message']['content']
    return response

def main():
    st.title("OpenAI GPT-3.5 Turbo Chatbot")

    messages = [{"role": "assistant", "content": "How can I help?"}]

    while True:
        display_chat_history(messages)

        user_input = st.text_input("User:")
        messages.append({"role": "user", "content": user_input})

        assistant_response = get_assistant_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()