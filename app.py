from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weather",  methods=['GET', 'POST'])
def get_weatherdata():
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    # querystring = {"q": "Toronto", "days": "3"}
    params = {
        "q" : request.args.get("city")
    }
    headers = {
        "X-RapidAPI-Key": "4ded612ff1mshfa97ab85255debep179561jsn0fae02ef241b",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)
    city=data['location']['name']
    temp=data['current']['temp_c']
    return f"City: {city}, Tempreture: {temp} "


if __name__=='__main__':
    app.run(host="localhost", port=5000)