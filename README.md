# Python Places API
## Table of Content
1. [Introduction](#introduction)
2. [Installation](#install)
3. [Live example](#example)
4. [API Docs](#api_docs)
5. [Special Notes](#notes)



## Introduction <a name="introduction"></a>
This is an API developed with Python using Flask and JWT in order to have secure routes.

## Installation <a name="install"></a>
  1. Clone this repository
  2. Run ``` pip install -r requirements.txt ``` in the root directory
  3. Run ```python app.py```

## Live Example <a name="example"></a>
There is a Live example for this API deployed in Heroku. In order to start you have to make a request to the following URI 
```
https://place-search-api.herokuapp.com/
```
## API Docs <a name="api_docs"></a>
The API routes are protected with JWT, so in order to use the routes, you need to login, to do this send a GET request with Basic Auth (see image)
![alt text](http://res.cloudinary.com/jrleon90/image/upload/v1528004591/login_comic_api.png "Postman example")
  The request has to be made to the following URI
  ```
 GET https://place-search-api.herokuapp.com/login
  ```
 Once the request has been made with a valid login information, it returns a token that needs to be save in order to made every request.
  
1. **GET PLACES**

Send GET request to
  ```
 GET https://place-search-api.herokuapp.com/search?location=<lat,lng>&radius=<radius in meters>&type=<type of the place>&keyword=<keyword to query the places>
  ```

Like the example above, the request needs to have the following required params:

    1.Location
  
    2.Radius
  
    3.Type
  
    4.Keyword

Since the routes are protected, the user needs to send the token in the header of the request with the key name "x-access-token" (see image)
![alt text](http://res.cloudinary.com/jrleon90/image/upload/v1528521554/get_place.png "Postman example")

The response it would be a JSON object with all the places from the requests of the Google Place's and Foursquare APIs.

2. **CREATE NEW USER**
  
 Send POST request to:
  
 ```
 POST https://place-search-api.herokuapp.com/user
 ```
  
With the request, send username and password inside the body in JSON format (see image)
  
  ![alt text](http://res.cloudinary.com/jrleon90/image/upload/v1528521734/user_place.png "Postman Example")

## Special Notes <a name='notes'></a>
There are requirements that could not been fulfilled since the APIs does not provide this information or it wasn't very clear, in particular there are to element missing: Provider and Description.

In case of the Provider, there wasn't too much information to make an assumption about it. With the description, there was no way to get this information since this field was deprecated from the current versions of the APIs

