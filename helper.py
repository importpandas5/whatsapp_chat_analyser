from wordcloud import WordCloud
import pandas as pd

def fetch_stats(selected_user,df):

    if selected_user != "Overall":
        df = df[df['user']==selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())

    return num_messages,len(words)


def create_wordcloud(selected_user,df):

    if selected_user != "Overall":
        df = df[df['user']==selected_user]

    wc = WordCloud(width=500,height=300,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))

    return df_wc.to_array()
