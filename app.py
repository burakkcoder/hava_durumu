from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Hava Durumu")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        sehir = yazi_alani.get()

        yer_bulucu = Nominatim(user_agent = "havaDurumu")
        lokasyon = yer_bulucu.geocode(sehir)

        obje = TimezoneFinder()
        sonuc = obje.timezone_at(lng = lokasyon.longitude, lat = lokasyon.latitude)

        konum = pytz.timezone(sonuc)
        yerel_zaman = datetime.now(konum)
        zaman = yerel_zaman.strftime('%H:%M')
        saat.config(text = zaman)
        baslik.config(text = "YEREL SAAT")

        #Hava Durumu
        api_key = "xxx"
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + sehir + "&appid=" + api_key + "&lang=tr"

        json_data = requests.get(api).json()
        print(json_data)
        tanim = json_data["weather"][0]["description"].title()
        sicaklik = int(json_data["main"]["temp"] - 273.15)
        basinc = json_data["main"]["pressure"]
        nem = json_data["main"]["humidity"]
        ruzgar = json_data["wind"]["speed"]

        s.config(text = (sicaklik, "°"))
        r.config(text = (ruzgar,"km/sa"))
        n.config(text = ("%",nem))
        t.config(text = tanim)
        b.config(text = (basinc,"hPa"))

    except Exception as e:
        messagebox.showerror("Hava Durumu", "Geçersiz Giriş!")


#Arama Kutusu
arama_kutusu_png = PhotoImage(file = "search.png")
arama_kutusu = Label(image = arama_kutusu_png)
arama_kutusu.place(x = 20, y = 20)

yazi_alani = tk.Entry(root, justify = "center", width = 17, font = ("poppins", 25, "bold"), bg = "#404040", border = 0, fg = "white")
yazi_alani.place(x = 50, y = 40)
yazi_alani.focus()

arama_iconu_png = PhotoImage(file = "search_icon.png")
arama_iconu = Button(image = arama_iconu_png, borderwidth = 0, cursor = "hand2", bg = "#404040", command = getWeather)
arama_iconu.place(x = 400, y = 34)

#Logo
logo_png = PhotoImage(file = "logo.png") 
logo = Label(image = logo_png)
logo.place(x = 150, y = 100)

#Alt Alan
alt_alan_png = PhotoImage(file = "box.png")
alt_alan = Label(image = alt_alan_png)
alt_alan.pack(padx = 5, pady = 5, side = BOTTOM)

#Zaman
baslik = Label(root, font = ("arial", 15, "bold"))
baslik.place(x = 30, y = 100)
saat = Label(root, font = ("Helvetica", 20))
saat.place(x = 30, y = 130)

#Alt Alan Labels
label1 = Label(root, text = "RÜZGAR", font = ("Helvetica", 15, "bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 130, y = 400)
label2 = Label(root, text = "NEM", font = ("Helvetica", 15, "bold"), fg = "white", bg = "#1ab5ef")
label2.place(x = 320, y = 400)
label3 = Label(root, text = "DURUM", font = ("Helvetica", 15, "bold"), fg = "white", bg = "#1ab5ef")
label3.place(x = 470, y = 400)
label4 = Label(root, text = "BASINÇ", font = ("Helvetica", 15, "bold"), fg = "white", bg = "#1ab5ef")
label4.place(x = 680, y = 400)

s = Label(font = ("arial", 70, "bold"), fg = "#ee666d")
s.place(x = 415, y = 150)
r = Label(text = "...", font = ("arial", 10, "bold"), bg = "#1ab5ef")
r.place(x = 130, y = 430)
n = Label(text = "...", font = ("arial", 10, "bold"), bg = "#1ab5ef")
n.place(x = 320, y = 430)
t = Label(text = "...", font = ("arial", 10, "bold"), bg = "#1ab5ef")
t.place(x = 470, y = 430)
b = Label(text = "...", font = ("arial", 10, "bold"), bg = "#1ab5ef")
b.place(x = 680, y = 430)

root.mainloop()
