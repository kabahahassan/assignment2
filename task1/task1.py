import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def foo():

    name = request.args["name"]
    URL1 = "https://restcountries.eu/rest/v2/name/"+name + "?fullText=true"
    r1 = requests.get(url=URL1)
    if r1.status_code != 200:
        return 'Error'
    data1 = r1.json()
    country = data1[0]
    currencyCode = country["currencies"][0]["code"]
    URL2 = "http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols="+currencyCode
    r2 = requests.get(url=URL2)
    data2 = r2.json()
    return jsonify([country["name"], country["capital"], country["languages"][0]["name"], country["currencies"][0]["name"], data2["rates"][currencyCode]])


app.run(host='0.0.0.0', debug=True, port=5000)
