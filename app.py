from flask import Flask
app = Flask(__name__)

from flask import render_template, jsonify, request
import requests
import json
import os

EBAY_APP_NAME = os.environ.get("EBAY_APP_NAME")
EBAY_AUTH_TOKEN = os.environ.get("EBAY_AUTH_TOKEN")

headers = {
    "content-type": "application/json",
    "X-EBAY-SOA-SECURITY-APPNAME": "".format(EBAY_APP_NAME),
    "Authorization": "Bearer {}".format(EBAY_AUTH_TOKEN)
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=['GET', 'POST'])
def search():
    # Retrieve parameters
    req_data = request.get_json()
    image = req_data['image']

    # Make API request 
    #   filter info here: https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html)
    #   key info here: https://developer.ebay.com/api-docs/buy/browse/resources/search_by_image/methods/searchByImage#uri.aspect_filter
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search_by_image/"
    if 'sort' in req_data.keys():
        url += "&sort={}".format(req_data['sort'])
    if 'limit' in req_data.keys():
        url += "&limit={}".format(req_data['limit'])
    if 'offset' in req_data.keys():
        url += "&offset={}".format(req_data['offset'])
    if 'aspect_filter' in req_data.keys():
        url += "&aspect_filter={}".format(req_data['aspect_filter'])
    if 'epid' in req_data.keys():
        url += "&epid={}".format(req_data['epid'])
    if 'category_ids' in req_data.keys():
        url += "&category_ids={}".format(req_data['category_ids'])
    
    payload = {
        "image": image,
        "item_filter": [
            {
                "name": "SoldItemsOnly",
                "value": "true"
            }
        ]
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    # Render Response
    return jsonify(json.loads(r.text))

@app.route("/insights/<item_id>", methods=['GET'])
def item(item_id):
    
    # Make API request
    url = "https://api.ebay.com/buy/marketplace-insights/v1/item_sales/search?epid={}&filter=lastSoldDate:[2018-08-30T00:00:00Z..2018-11-07T00:00:00Z]".format(item_id)
    r = requests.post(url, headers=headers)

    # Render Response
    return jsonify(json.loads(r.text))