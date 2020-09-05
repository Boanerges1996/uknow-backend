from flask import request, current_app as app
import jwt
from functools import wraps


def authentication_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        if 'auth-token' in request.headers:
            token = request.headers['auth-token']

        if not token:
            return {
                "message": "login to access this route"
            }, 401
        try:
            decode_token = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return {
                "user-token": "invalid"
            }, 401
        return f(*args, **kwargs)

    return wrap
