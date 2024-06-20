import yfinance as yf

def stocks(nama):
    nama = nama.upper()
    try:
        get = yf.Ticker(nama)
        info = get.info
        long_name = info.get('longName', 'N/A')
        print(long_name)
        return get.history(period='6mo') 
    
    except Exception as e:
        print(f"kode {nama} tidak ada dalam database Yahoo Finance {e}")



