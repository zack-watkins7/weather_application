from ast import Lambda
import requests
import os
import tkinter as tk
from tkinter import font


API_key= os.environ['weather_api_key']




#City_Data= requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={requested_city},uk&APPID={API_key}')

def format_response(weather):
    Name= weather['name']
    description= weather['weather'][0]['description']
    temperature= weather['main']['temp']

    return str(Name) +' '+ str(description) +' '+ str(temperature)



def weather_data(city):
    weather_key= os.environ['weather_api_key']
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID': weather_key, 'q': city, 'units': 'imperial'}    
    response= requests.get(url, params=params)
    weather= response.json()

    display_information['text']= format_response(weather)

#Global Variables
HEIGHT=600
WIDTH= 800
top= tk.Tk() # All the main code goes inside of here.




window= tk.Canvas(top, height=HEIGHT, width=WIDTH)
window.pack()

background_image = tk.PhotoImage(file='windmill.gif')
background_label = tk.Label(top, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame= tk.Frame(top, bg='#cc6600')
frame.place(relx=0.3, rely=0.2,relwidth=0.4, relheight=0.05)

user_city=tk.Entry(frame)
user_city.place(relx=0.05,rely=0.2,relwidth=0.5,relheight=0.55)


information_frame= tk.Frame(top, bg='#C17B6C',bd=10)
information_frame.place(relx=0.3, rely=0.26,relwidth=0.4,relheight=0.4)


button=tk.Button(frame, text='Get Weather!', font=('High Tower Text',11), command=lambda: weather_data(user_city.get()))
button.place(relx=0.65,rely=0.2,relwidth=0.3, relheight= 0.55)

display_information= tk.Label(information_frame)
display_information.place(relwidth=1, relheight=1)



top.mainloop()