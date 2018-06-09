from app import app,db
from flask import request,make_response,jsonify
from APIs.central_node import *
from functools import wraps
import jwt
import datetime
from werkzeug.security import generate_password_hash,check_password_hash

#Function to validate Token
def token_verification(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        #Search for token inside the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        #If there is no token, send response with message
        if not token:
            return make_response('Token is missing', 401,{'WWW-authenticate' : 'Basic realm="Login required!"'})

        #Decode token and find get information of the current user
        try:
            token_decoded = jwt.decode(token,app.config['SECRET_KEY'])


        #if token expired, send messages and abort the process
        except jwt.ExpiredSignature:
            return make_response('Token expired', 401,{'WWW-authenticate' : 'Basic realm="Login required!"'})
      
        #If there is an error in the password, send message and abort process
        except jwt.DecodeError:
            return make_response('Could not decode token', 401,{'WWW-authenticate' : 'Basic realm="Login required!"'})
      
        return f(*args,**kwargs)
   
    return decorated


@app.route('/', methods=['GET'])
def index():
    return jsonify({"Message":"Welcome to the Place's search API!"})

@app.route('/search',methods=['GET'])
@token_verification
def search_place():
    data = request.args.to_dict()
    response = getData(data)

    return response

@app.route('/user',methods=['POST'])
def create_user():
    data = request.get_json()
    hashPassword = generate_password_hash(data['password'],method='sha256')
    db.users.insert_one({
        'username':data['username'],
        'password':hashPassword
    })
    return jsonify({'message': 'User added'})

@app.route('/login',methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('No username or password',401)

    user = db.users.find_one({'username':auth.username})

    if not user:
        return make_response('User not found',401)
    
    if check_password_hash(user['password'],auth.password):
        token = jwt.encode({'username':auth.username,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30 )},app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify',401)