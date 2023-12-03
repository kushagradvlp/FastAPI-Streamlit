import pickle
import nltk
from fastapi import FastAPI
app=FastAPI()

@app.post("/")
def get_name(text='Sample text'):
    return {'Name':text}

with open('sentiment_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.post("/analyse/sentiment")
def analyse_sentiment(text: str):
    return model.polarity_scores(text)