from huggingface_hub import InferenceClient

client = InferenceClient(
	provider="hf-inference",
	api_key="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"
)

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="mistralai/Mistral-Nemo-Instruct-2407", 
	messages=messages, 
	max_tokens=500
)

st.title("генерация текста") 
st.write(f"{completion.choices[0].message}")