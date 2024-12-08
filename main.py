import openai
from langchain_openai import ChatOpenAI

openai.api_key = "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"

# ChatOpenAI 객체 생성 시 API 키 전달
chat_model = ChatOpenAI(api_key=openai.api_key)

# 모델 호출
subject = "AI"
result = chat_model.invoke(subject + "에 대한 시를 써줘.")
print(result.content)

import streamlit as st

st.title("인공지능 시인")