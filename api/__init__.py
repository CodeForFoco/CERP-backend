"""
    This file is used to initalize the application
"""
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('config')

# This allows Cross-Origin-Requests,
# the `supports_credentials` allows for sessions
# not sure if needed, but I'll have it in case we
# decide login is a thing
cors = CORS(app, supports_credentials=True)

# I know it's weird, but this needs to be at the bottom
from api import views
