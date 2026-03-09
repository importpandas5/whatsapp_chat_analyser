import streamlit as st
import preprocessor
import helper
import pandas as pd

st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

st.title("📊 WhatsApp Chat Analyzer")

uploaded_file = st.file_uploader("Upload WhatsApp Chat TXT File")

if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis for",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages, words = helper.fetch_stats(selected_user,df)

        col1,col2 = st.columns(2)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        st.title("Word Cloud")
        wc = helper.create_wordcloud(selected_user,df)
        st.image(wc)
