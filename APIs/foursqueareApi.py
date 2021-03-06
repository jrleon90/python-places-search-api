from flask import jsonify,make_response,request
import requests
from app import app

def getFoursquareData(data):
    foursquareData = requests.get('https://api.foursquare.com/v2/venues/search?client_id='+app.config['FOURSQUARE_CLIENT_ID']+'&client_secret='+app.config['FOURSQUARE_CLIENT_SECRET']+'&v='+app.config['FOURSQUARE_VERSION']+'&ll='+data['location']+'&query='+data['keyword']+'&radius='+data['radius'])
    foursquareDataJson = foursquareData.json()
    responseData = []
    for item in foursquareDataJson['response']['venues']:
        outputData = {}
        outputData['data'] = {}   
        placeDetail = requests.get('https://api.foursquare.com/v2/venues/'+item['id']+'?client_id='+app.config['FOURSQUARE_CLIENT_ID']+'&client_secret='+app.config['FOURSQUARE_CLIENT_SECRET']+'&v='+app.config['FOURSQUARE_VERSION'])
        placeDetailJson = placeDetail.json()

        outputData['data']['foursquare_latitude'] = item['location']['lat']
        outputData['data']['foursquare_longitude'] = item['location']['lng']
        if 'address' in item['location']:
            outputData['data']['foursquare_address'] = item['location']['address']
        if 'url' in placeDetailJson['response']['venue']:
            outputData['data']['foursquare_website'] = placeDetailJson['response']['venue']['url']
        outputData['foursquare_id'] = item['id']
        outputData['foursquare_name'] = item['name']
        responseData.append(outputData)

        

    return responseData