import streamlit as st
import time
from stock_analysis import analyze_stock  # Import the modified external code
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 100px;
}
</style>
""",
    unsafe_allow_html=True,
)

def display_analysis(stock_code, period):
    try:
        # Pastikan jumlah variabel sesuai dengan jumlah nilai yang dikembalikan
        fig, real_price, price_predict, sentiment_analysis, nama_company = analyze_stock(stock_code, period)
        
        # Memperbesar ukuran plot
        fig.set_size_inches(15, 8)  # Atur ukuran sesuai kebutuhan Anda
        
        st.write(f'<p style="font-size:56px;"{nama_company}</p>', unsafe_allow_html=True)
        st.write(f'<p style="font-size:20px;">Current Price: ${real_price:.2f}</p>', unsafe_allow_html=True)

        # Display the plot
        canvas = FigureCanvas(fig)
        st.pyplot(fig, use_container_width=True)  # Membuat plot lebih besar
        selisih = price_predict-real_price
        selisih = f'{selisih:.2f}'
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label = 'Price Prediction', value = f"$ {price_predict:.2f}", delta=selisih)
            # st.write(f"Prediction Price: ${price_predict:.2f}")
        with col2:
            st.write(r"$\textsf{\Large Sentiment Analysis}$")
            if sentiment_analysis == "Up":
                st.image('assets/naik.gif')
            elif sentiment_analysis == "Neutral":
                st.image('assets/netral.gif')
            else:
                st.image('assets/Down.gif')
            st.write(f'<p style="font-size:20px;">Current Price: ${sentiment_analysis}</p>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

def How_To():
    st.markdown("<h1 style='text-align: center;'>How To Use</h1>", unsafe_allow_html=True)
    st.image('assets/contoh_bitcoin.png', caption='Example: BTC-USD', use_column_width=True)
    st.write(
        """
        <div style="word-wrap: break-word; font-size: 24px">
            <p>This program is used to analyze stock and currency prices using data sourced from <a href='https://finance.yahoo.com/' target='_blank'>Yahoo Finance</a>. Here are the steps to use the program:</p>
            <ol>
                <li>Enter the stock code you want to analyze in the provided input field. For example, you can use the code <strong>BTC-USD</strong> as shown in the image above.</li>
                <li>Select the desired analysis period from the available options (e.g., 1 month, 3 months, 6 months, 1 year, etc.).</li>
                <li>Click the "Submit" button to start the analysis. The program will process the data and display the analysis results, including price predictions and sentiment analysis.</li>
                <li>If you want to exit the analysis, click the "Exit" button.</li>
            </ol>
            <p>The data used in this analysis is sourced from <a href='https://finance.yahoo.com/' target='_blank'>Yahoo Finance</a>, which provides real-time and historical stock price information.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_model():
    st.markdown("<h1 style='text-align: center;'>Model Information</h1>", unsafe_allow_html=True)
    col_1, col_2 = st.columns(2)
    with col_1:
        st.write(r"$\textsf{\LARGE Logistic Regression.}$")
        st.write(
            """
            <div style="word-wrap: break-word;font-size: 20px">
                Logistic Regression is used to analyze stock prices obtained from the Yahoo Finance dataset. In this case, the only feature (X) used is the stock price itself. The goal is to predict whether the stock price will go up or down based on its historical values.
            </div>
            """,
            unsafe_allow_html=True
        )   
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("assets/logistic_plot.png", caption="Logistic Regression Plot", use_column_width=True)
        st.image("assets/logistic_result.png", caption="Logistic Regression Metrics", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_2:
        st.write(r"$\textsf{\LARGE Naive Bayes.}$")
        st.write(
            """
            <div style="word-wrap: break-word;font-size: 20px">
                Naive Bayes is used to analyze sentiment on Twitter/X. This algorithm helps in classifying tweets into different sentiment categories (e.g., positive, neutral, negative) based on the text content. By applying the Naive Bayes theorem, the model estimates the probability of a tweet belonging to a particular sentiment class, making it a powerful tool for text classification tasks.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image("assets/classification_result.png", caption="Naive Bayes Metrics", use_column_width=True)

def analisa_page():
    st.markdown("<h1 style='text-align: center;'>Prediction Price of Stock and Currency</h1>", unsafe_allow_html=True)
    stock_code = st.text_input(r"$\textsf{\Large Enter Code}$")
    period = st.select_slider(
        r"$\textsf{\Large Select Analysis Period:}$",
        options=['1mo', '3mo', '6mo','1y','2y','3y']
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit", key="submit_button", use_container_width=True):
            if stock_code:
                with st.spinner('Loading analysis, please wait...'):
                    display_analysis(stock_code, period)
            else:
                st.error("Invalid stock code. Please try again.")

    with col2:
        if st.button("Exit", key="exit_button", use_container_width=True):
            st.stop()


if st.sidebar.button("How to Use"):
    st.session_state.page = "How"
if st.sidebar.button("Analysis"):
    st.session_state.page = "Analysis"
if st.sidebar.button("Model"):
    st.session_state.page = "Model"

if "page" in st.session_state:
    if st.session_state.page == "How":
        How_To()
    elif st.session_state.page == "Analysis":
        analisa_page()
    elif st.session_state.page == "Model":
        display_model()
else:
    st.session_state.page = "How"
    How_To()

# CSS untuk memperlebar konten
page_bg_img = '''
<style>
    .stApp {
        background-image: url("");
        background-size: cover;
    }
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 250px;
        }
        .stButton button {
            width: 100%;
            height: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)