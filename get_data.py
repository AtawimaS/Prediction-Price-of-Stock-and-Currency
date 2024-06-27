import yfinance as yf
import requests
from requests.exceptions import HTTPError

def stocks(nama, periode):
    nama = nama.upper()
    try:
        get = yf.Ticker(nama)
        info = get.info
        long_name = info.get('longName', 'N/A')
        return get.history(period=periode) , long_name
    
    except Exception as e:
        print(f"kode {nama} tidak ada dalam database Yahoo Finance {e}")
