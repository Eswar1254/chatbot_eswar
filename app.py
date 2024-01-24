# app.py
import streamlit as st
import openai
import os

# Set your OpenAI API key using environment variable
openai.api_key = os.environ.get("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")

def display_chat_history(messages):
    for message in messages:
        st.write(f"{message['role'].capitalize()}: {message['content']}")

def get_assistant_response(messages):
    try:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        )
        response = r['choices'][0]['message']['content']
        return response
    except openai.error.AuthenticationError as e:
        st.error(f"Authentication Error: {e}")
        st.stop()
    except openai.error.OpenAIError as e:
        st.error(f"OpenAI Error: {e}")
        st.stop()

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
