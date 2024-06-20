import os
import re
import pickle
import nltk
import sys
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, parent_dir)

import get_data

from NgambilAPI import TwitterScraper as TS

def analyze_stock(find="btc-usd"):
    # Scrape Twitter data
    scraper = TS(find, num=5)
    ini = scraper.scrape(dataframe=True)
    
    # Download NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    
    # Clean text function
    def clean_text(text):
        text = re.sub(r'[^\w\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        cleaned_text = ' '.join(tokens)
        return cleaned_text
    
    ini['Message'] = ini['Message'].apply(clean_text)
    
    # Load models and vectorizer
    path = os.path.join('sentimen_analisis_model','NB.pickle')
    with open(path, 'rb') as file:
        model = pickle.load(file)
    
    path = os.path.join('sentimen_analisis_model','vectorizer.pkl')
    with open(path, 'rb') as file:
        vectorizer = pickle.load(file)
    
    path = os.path.join('Logistic_regression_model', 'LR.pickle')
    with open(path,'rb') as file:
        LR = pickle.load(file)
    
    x = vectorizer.transform(ini['Message'])
    prediction = model.predict(x)
    
    LE = LabelEncoder()
    LE.fit(['negative', 'neutral', 'positive'])
    sentiment = LE.transform(prediction)
    
    hitung = sum(sentiment)
    sentimentnya = hitung / len(sentiment)
    
    df = get_data.stocks(find)
    data = df.reset_index()
    date = data['Date']
    X = data[['Close']]
    y_pred = LR.predict(X)
    
    real_price = float(X['Close'].iloc[-1])
    price_predict = float(y_pred[-1])
    
    if sentimentnya > 1.5:
        sentiment_analysis = "Naik"
    elif sentimentnya < 1.5 and sentimentnya > 1:
        sentiment_analysis = "Netral"
    else:
        sentiment_analysis = "Turun"
    
    fig, ax = plt.subplots()
    ax.scatter(date, X)
    ax.plot(date, y_pred, color="Red")
    
    return fig, real_price, price_predict, sentiment_analysis
