import jwt
from functools import wraps
from flask import Blueprint, request, make_response, current_app
from werkzeug.security import check_password_hash
from app.db import users_table as db
from datetime import datetime, timedelta


bp = Blueprint('security', __name__)


@bp.route('/login',methods=(['POST']))
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    error = None

    try:
        user = db[username]
    except:
        user = None

    if user is None or not check_password_hash(user['password'], password):
        error = 'Incorrect user or password'

    if error is None:
        payload = {
            'iat': datetime.utcnow(),                          # Current time
            'exp': datetime.utcnow() + timedelta(minutes=10),  # Expiration time
            'sub': user['name'],
            'rol': user['rol']
        }
        return make_response(jwt.encode(payload, current_app.config['SECRET_KEY'],algorithm='HS256'), 200)

    return make_response(error, 401)


def token_required(rol):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return make_response('Invalid credentials', 401)
            
            try:
                data = jwt.decode(token, current_app.config['SECRET_KEY'])
            except:
                return make_response('Invalid credentials', 401)
            
            if rol != data['rol']:
                return make_response('Invalid role', 403)

            return f(*args, **kwargs)
        return decorated

    return decorator
