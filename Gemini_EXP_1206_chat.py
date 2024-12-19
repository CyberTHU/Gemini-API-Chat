#(1)先安装：pip install google-generativeai
#(2)直接对话或进行改造(history中存储上下文)
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBjD1qB4dk-hzP96_K0hbZKMRtd1DbcBes")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-exp-1206",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(input())

print(response.text)
