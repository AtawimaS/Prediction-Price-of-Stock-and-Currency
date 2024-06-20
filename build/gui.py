import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *
import customtkinter
import threading
import turtle
import colorsys
from stock_analysis import analyze_stock  # Import the modified external code


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"
ASSETS_PATH = ASSETS_PATH.resolve()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def enter_stock_code():
    stock_code = stock_code_entry.get()
    if stock_code:
        analysis_done.clear()
        threading.Thread(target=display_analysis, args=(stock_code,)).start()
        threading.Thread(target=loading_animation).start()
    else:
        messagebox.showerror("Error", "Invalid stock code. Please try again.")


def display_analysis(stock_code):
    fig, real_price, price_predict, sentiment_analysis, nama_company = analyze_stock(stock_code)
    
    # Update labels with real price, prediction price, and sentiment analysis
    nama_company_label.config(text=f"{nama_company}")
    real_price_label.config(text=f"Current Price: $ {real_price:.2f}")
    predict_price_label.config(text=f"Prediction Price: $ {price_predict:.2f}")
    sentiment_analysis_label.config(text=f"Sentiment Analysis: {sentiment_analysis}")
    
    # Display the plot in the main frame
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    analysis_done.set()
    switch_to_main_frame()


def loading_animation():
    t.hideturtle()
    t.pensize(8)
    t.pencolor('white')
    t.speed(5)  
    screen.tracer(0, 0)
    while not analysis_done.is_set():
        for i in range(48):
            t.color(colorsys.hls_to_rgb(i / 48, i/48, 1))
            t.forward(8)
            t.right(6)
            if i % 2 == 0:
                t.penup()
            else:
                t.pendown()
    t.clear()
    screen.update()

def switch_to_main_frame():
    login_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)


def go_back():
    main_frame.pack_forget()
    login_frame.pack(fill='both', expand=True)


def exit_application():
    window.quit()


# Set up the main window
window = Tk()

window_width = 800
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
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
stock_code_entry.pack(pady=20)

customtkinter.CTkButton(
    login_frame,
    text="Submit",
    command=enter_stock_code,
    font=("TitilliumWeb Regular", 16)
).pack(pady=5)

customtkinter.CTkButton(
    login_frame,
    text="Exit",
    command=exit_application,
    hover_color="#FFFFFF",
    font=("TitilliumWeb Regular", 16)
).pack()

# Create the main frame
main_frame = Frame(window, bg="#FFFFFF")

# Add labels for displaying analysis results
nama_company_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 24))
nama_company_label.pack(pady=5)

real_price_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 14))
real_price_label.pack(pady=3)

predict_price_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 14))
predict_price_label.pack(pady=3)

sentiment_analysis_label = Label(main_frame, text="", bg="#FFFFFF", font=("TitilliumWeb Regular", 14))
sentiment_analysis_label.pack(pady=3)

customtkinter.CTkButton(
    main_frame,
    text="Back",
    command=go_back,
    font=("TitilliumWeb Regular", 16)
).pack(pady=10)

customtkinter.CTkButton(
    main_frame,
    text="Exit",
    command=exit_application,
    font=("TitilliumWeb Regular", 16)
).pack()

canvas = Canvas(login_frame, width=400, height=400, highlightthickness=0)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
screen.bgcolor("#FFFFFF")

analysis_done = threading.Event()

window.resizable(False, False)
window.mainloop()
