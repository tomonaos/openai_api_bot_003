
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


MAX_CHAT = 40

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀な面接官です。就活生の回答に対して適切な質問をしてください。"},
        {"role": "assistant", "content": "それでは面接を始めます。まずは自己紹介をお願いします。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去



# ユーザーインターフェイスの構築
st.title("AI面接官")

st.caption("AI面接官です")

if st.session_state["messages"]:
    messages = st.session_state["messages"]
    message(messages[-1]["content"]) 


if st.session_state["messages"]:
    messages = st.session_state["messages"]
    if len(messages) < MAX_CHAT:
        user_input = st.text_input("", key="user_input", max_chars=200, on_change=communicate)

    for message in messages[2:]:  # 
        
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])

