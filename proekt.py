from huggingface_hub import InferenceClient
import streamlit as st

client = InferenceClient(
	provider="hf-inference",
	api_key="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"
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