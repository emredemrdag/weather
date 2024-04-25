from tkinter import *
from PIL import ImageTk, Image

import requests

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "d66e048b0f4e67cc9ade78c9f6425612"
icon_url = "https://openweathermap.org/img/wn/{}@2x.png"

def get_weather(city):
    param = {"q": city, "appid": api_key,"lang": "EN"}
    data = requests.get(url, params=param).json()
    if data:
        city = data["name"].capitalize()
        country = data["sys"]["country"]
        temp = int(data["main"]["temp"] - 273.15)
        icon = data["weather"][0]["icon"]
        condition = data["weather"][0]["description"]
        return(city, country, temp, icon, condition)

def main():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        location_label["text"] = "{},{}".format(weather[0], weather[1])
        temp_label["text"] = "{}°C".format(weather[2])
        condition_label["text"] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]), stream=True).raw))
        icon_label.configure(image= icon)
        icon_label.image = icon

screen = Tk()
screen.geometry("350x450")
screen.title("weather")

city_entry = Entry(screen, justify="center")
city_entry.pack(fill=BOTH, ipady=10, padx=18, pady=5)
city_entry.focus()

search_button = Button(screen, text="search", font=("Arial",15), command=main)
search_button.pack(fill=BOTH, ipady=10, padx=20)

icon_label = Label(screen)
icon_label.pack()

location_label = Label(screen, font=("Arial", 40))
location_label.pack()

temp_label = Label(screen, font=("Arial", 50, "bold"))
temp_label.pack()

condition_label = Label(screen, font=("Arial", 20))
condition_label.pack()

screen.mainloop()
