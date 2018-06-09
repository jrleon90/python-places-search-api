from flask import jsonify,make_response,request
import requests
from app import app

def getGoogleData(data):
    googleData = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+data['location']+'&radius='+data['radius']+'&type='+data['type']+'&keyword='+data['keyword']+'&key='+app.config['GOOGLE_PLACE_KEY'])
    dataJson = googleData.json()
    responseData = []

    for item in dataJson['results']:
        outputData = {}
        placeDetail = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+item['place_id']+'&key='+app.config['GOOGLE_PLACE_KEY'])
        placeDetailJson = placeDetail.json()
        outputData['google_place_latitude'] = item['geometry']['location']['lat']
        outputData['google_place_longitude'] = item['geometry']['location']['lng']
        outputData['google_place_address'] = item['vicinity']
        if 'website' in placeDetailJson['result']:
            outputData['google_place_website'] = placeDetailJson['result']['website']
        
        outputData['google_place_id'] = item['place_id']
        outputData['google_place_name'] = item['name']        
        responseData.append(outputData)


    return responseData