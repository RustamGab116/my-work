from huggingface_hub import InferenceClient
import streamlit as st
from mistral_inference.transformer import Transformer
from mistral_inference.generate import generate
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest

from openai import OpenAI

client = OpenAI(
	base_url="https://api-inference.huggingface.co/v1/",
	api_key="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"
)

#client = InferenceClient(
#	provider="hf-inference",
#	api_key="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"
#)

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