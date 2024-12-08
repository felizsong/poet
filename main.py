from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

# ChatOpenAI 객체 생성 시 API 키 전달
chat_model = ChatOpenAI()

# 모델 호출
subject = "AI"
result = chat_model.invoke(subject + "에 대한 시를 써줘.")
print(result.content)

import streamlit as st

st.title("인공지능 시인")