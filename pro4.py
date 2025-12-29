import requests
import threading
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "ce0abd09ab1940c6b3a135237251112"   # ← Put your key here
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

# ---------------- FUNCTIONS ---------------- #

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "days": 3,       # 3-day forecast
        "aqi": "no",
        "alerts": "no"
    }
    r = requests.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def on_get_weather_threaded():
    threading.Thread(target=on_get_weather, daemon=True).start()


def on_get_weather():
    city = city_var.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        data = get_weather(city)
    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")
        return

    # ---- Extract current ---- #
    loc = data["location"]
    curr = data["current"]

    country = loc["country"]
    name = loc["name"]

    cond_text = curr["condition"]["text"]
    icon_url = "https:" + curr["condition"]["icon"]

    # Unit toggle
    if unit_var.get() == "C":
        temp = f"{curr['temp_c']} °C"
    else:
        temp = f"{curr['temp_f']} °F"

    humidity = curr["humidity"]
    wind = curr["wind_kph"]

    # Update UI (use root.after for thread safety)
    root.after(0, lambda: label_city.config(text=f"{name}, {country}"))
    root.after(0, lambda: label_temp.config(text=f"Temperature: {temp}"))
    root.after(0, lambda: label_condition.config(text=f"Condition: {cond_text}"))
    root.after(0, lambda: label_humidity.config(text=f"Humidity: {humidity}%"))
    root.after(0, lambda: label_wind.config(text=f"Wind: {wind} kph"))

    # ---- Download icon ---- #
    try:
        icon_data = requests.get(icon_url).content
        img = Image.open(BytesIO(icon_data)).resize((70,70))
        photo = ImageTk.PhotoImage(img)
        root.after(0, lambda: icon_label.config(image=photo))
        icon_label.image = photo
    except:
        root.after(0, lambda: icon_label.config(image=""))

    # ---- Handle Forecast ---- #
    forecast = data["forecast"]["forecastday"]

    # Clear previous items
    for widget in forecast_frame.winfo_children():
        widget.destroy()

    for i, day in enumerate(forecast):
        f = Frame(forecast_frame, bg="#F7FAFC", bd=1, relief="ridge", padx=8, pady=8)
        f.grid(row=0, column=i, padx=10)

        # Day name
        day_label = Label(f, text=day["date"], font=("Arial", 10, "bold"), bg="#F7FAFC")
        day_label.pack()

        condition = day["day"]["condition"]["text"]
        icon_f = "https:" + day["day"]["condition"]["icon"]

        # Temperature
        if unit_var.get() == "C":
            temp_d = f"{day['day']['avgtemp_c']} °C"
        else:
            temp_d = f"{day['day']['avgtemp_f']} °F"

        # Icon
        try:
            icon_data_f = requests.get(icon_f).content
            img_f = Image.open(BytesIO(icon_data_f)).resize((50,50))
            photo_f = ImageTk.PhotoImage(img_f)
            icon_lbl = Label(f, image=photo_f, bg="#F7FAFC")
            icon_lbl.image = photo_f
            icon_lbl.pack()
        except:
            pass

        Label(f, text=condition, bg="#F7FAFC", font=("Arial", 9)).pack()
        Label(f, text=temp_d, bg="#F7FAFC", font=("Arial", 9, "bold")).pack()


# ---------------- GUI ---------------- #

root = Tk()
root.title("Advanced Weather App")
root.geometry("500x520")
root.config(bg="#E8F0FE")

title = Label(root, text="🌤 Weather App", font=("Arial", 18, "bold"), bg="#E8F0FE")
title.pack(pady=10)

# Input Frame
frame = Frame(root, bg="#E8F0FE")
frame.pack(pady=5)

city_var = StringVar()
Entry(frame, textvariable=city_var, font=("Arial", 12), width=25).grid(row=0, column=0, padx=10)

Button(frame, text="Get Weather", command=on_get_weather_threaded, font=("Arial", 11)).grid(row=0, column=1)

# Unit toggle
unit_var = StringVar(value="C")
Radiobutton(root, text="°C", variable=unit_var, value="C", bg="#E8F0FE").pack()
Radiobutton(root, text="°F", variable=unit_var, value="F", bg="#E8F0FE").pack()

# Output
icon_label = Label(root, bg="#E8F0FE")
icon_label.pack(pady=5)

label_city = Label(root, text="", font=("Arial", 14, "bold"), bg="#E8F0FE")
label_city.pack()

label_temp = Label(root, text="", font=("Arial", 12), bg="#E8F0FE")
label_temp.pack()

label_condition = Label(root, text="", font=("Arial", 12), bg="#E8F0FE")
label_condition.pack()

label_humidity = Label(root, text="", font=("Arial", 12), bg="#E8F0FE")
label_humidity.pack()

label_wind = Label(root, text="", font=("Arial", 12), bg="#E8F0FE")
label_wind.pack()

# Forecast section
Label(root, text="3-Day Forecast", font=("Arial", 14, "bold"), bg="#E8F0FE").pack(pady=10)

forecast_frame = Frame(root, bg="#E8F0FE")
forecast_frame.pack()

root.mainloop()
