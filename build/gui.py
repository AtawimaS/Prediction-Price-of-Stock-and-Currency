import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *
import customtkinter
from stock_analysis import analyze_stock  # Import the modified external code

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Semester_4\Machine Learning\Code\Setiment_Analysis_with_Scraping_Threads\Setiment_Analysis_with_Scraping_Threads\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def enter_stock_code():
    stock_code = stock_code_entry.get()
    if stock_code:
        login_frame.pack_forget()
        main_frame.pack(fill='both', expand=True)
        display_analysis(stock_code)
    else:
        messagebox.showerror("Error", "Invalid stock code. Please try again.")

def display_analysis(stock_code):
    fig, real_price, price_predict, sentiment_analysis = analyze_stock(stock_code)
    
    # Update labels with real price, prediction price, and sentiment analysis
    real_price_label.config(text=f"Current Price: $ {real_price:.2f}")
    predict_price_label.config(text=f"Prediction Price: $ {price_predict:.2f}")
    sentiment_analysis_label.config(text=f"Sentiment Analysis: {sentiment_analysis}")
    
    # Display the plot in the main frame
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

# Set up the main window
window = Tk()
window.geometry("730x400")
window.configure(bg="#FFFFFF")

# Create the login frame
login_frame = Frame(window, bg="#FFFFFF")
login_frame.pack(fill='both', expand=True)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

Label(
    login_frame,
    text="Silahkan Masukan Kode Saham",
    bg="#FFFFFF",
    font=("TitilliumWeb Regular", 20)
).pack(pady=20)

stock_code_entry = Entry(
    login_frame,
    text="Silahkan Masukan Kode Saham",
    bd=0,
    bg="#F3F3F3",
    highlightthickness=0,
    font=("TitilliumWeb Regular", 16)
)
stock_code_entry.pack(pady=10)

customtkinter.CTkButton(
    login_frame,
    text="Submit",
    command=enter_stock_code,
    # bg="#4CAF50",
    # fg="#C850C0",
    font=("TitilliumWeb Regular", 16)
).pack(pady=20)

# Create the main frame
main_frame = Frame(window, bg="#FFFFFF")

# Add labels for displaying analysis results
real_price_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 16))
real_price_label.pack(pady=5)

predict_price_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 16))
predict_price_label.pack(pady=5)

sentiment_analysis_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 16))
sentiment_analysis_label.pack(pady=5)

window.resizable(False, False)
window.mainloop()
