import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = text.lower()
    return text

def create_dataframe(posts):
    posts_df = pd.DataFrame(posts, columns=['text'])
    posts_df['text'] = posts_df['text'].apply(clean_text)
    return posts_df
