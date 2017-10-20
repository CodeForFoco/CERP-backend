"""
    The controls all the API endpoints
"""
from api import app
# common flask imports (for later) render_template, request, session,
# redirect, url_for
from flask import jsonify


@app.route('/')
def index():
    """ if someone hits the root dir, return just a simple result:true """
    return jsonify(result=True)


@app.route('/pieme')
def pieme():
    """
        Sample endpoint, showing how the application will
        work with the front end
    """
    return jsonify([
        [2235235101, ['Trump/Pence', 289], ['Clinton/Kaine', 359]],
        [2235235102, ['Trump/Pence', 115], ['Clinton/Kaine', 98]],
        [2145235201, ['Trump/Pence', 385], ['Clinton/Kaine', 727]],
        [2234935809, ['Trump/Pence', 681], ['Clinton/Kaine', 251]],
        [2234935810, ['Trump/Pence', 977], ['Clinton/Kaine', 523]]])
