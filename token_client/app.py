import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

from token_client.validator import Auth0JWTBearerTokenValidator
from authlib.integrations.flask_oauth2 import ResourceProtector

app = Flask(__name__)

load_dotenv()

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    os.getenv("AUTH_API_URI"),
    os.getenv("AUDIENCE"),
)
require_auth.register_token_validator(validator)


@app.route("/api/token")
def get_token():
    auth_token = request.headers.get("Authorization")

    return jsonify({"token": auth_token})
