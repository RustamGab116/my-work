import streamlit as st
from openai import OpenAI

client = OpenAI(
	base_url="https://api-inference.huggingface.co/v1/",
	api_key="hub key"
)


zapros = st.text_input("Запрос", "Life of Brian")

messages = [
	{
		"role": "user",
		"content": zapros
	}
]

completion = client.chat.completions.create(
    model="mistralai/Mistral-Nemo-Instruct-2407", 
	messages=messages, 
	max_tokens=500
)

st.title("генерация текста") 
st.write(f"{completion.choices[0].message}")