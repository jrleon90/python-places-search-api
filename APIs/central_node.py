from flask import jsonify,make_response,request
from APIs import googlePlaceApi,foursqueareApi


def getData (data):

    googleData = googlePlaceApi.getGoogleData(data)
    foursqueareData = foursqueareApi.getFoursquareData(data)

    return jsonify({'foursquare_data': foursqueareData,'google_place': googleData})

