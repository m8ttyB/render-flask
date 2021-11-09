import bike

from flask import Flask

app = Flask(__name__)
data = {
  "bike01": {
    "name": "NW Bikes - Reaper 24",
    "in_stock": None,
    "url": "https://northwestbicycle.com/products/2021-rocky-mountain-reaper-24",
    "msg": ""
  },
  "bike02": {
    "name": "NW Bikes - Reaper 26",
    "in_stock": None,
    "url": "https://northwestbicycle.com/collections/2021-rocky-mountain/products/2021-rocky-mountain-reaper-26",
    "msg": ""
  }
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bikes')
def check_bike_status():
    return bike.check_bikes(data)
