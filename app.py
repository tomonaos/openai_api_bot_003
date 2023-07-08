
import streamlit as st
from streamlit_chat import message
import openai
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
import langchain

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

###chat = ChatOpenAI(temperature=0)
##response = chat([HumanMessage(content="Translate this sentence from English to Japanese. I love drinking beer.")])

# ユーザーインターフェイスの構築
st.title("AI面接官")
st.caption("AI面接官です")

