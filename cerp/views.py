"""
    The controls all the endpoints
"""
from flask import jsonify, render_template
from cerp import app, data


@app.errorhandler(404)
def pageNotFound(error):
    return jsonify(result=False, reason="Page Not Found")


@app.errorhandler(500)
def ise(error):
    return jsonify(result=False, reason="Internal Server Error")


@app.route('/')
def index():
    """
        Return the index page. Which loads the vue application
    """
    return render_template('index.html')


@app.route("/api")
def api():
    """ If someone hits root api dir, show them all paths """
    return jsonify(result=True, paths=sorted(
        [str(rule) for rule in app.url_map.iter_rules()]
    ))


@app.route("/api/topics")
def topics():
    """ List all topics available """
    return jsonify(result=True, topics=sorted(data.ELECTION_DATA.keys()))


@app.route('/api/<topic>/<precinctNum>/pie')
def topic_pie(topic, precinctNum):
    """
        Generate a highcharts pie friendly dataset

        output:
            [
                [
                    'Vote1' (str),
                    value (int)
                ],
                [
                    'Vote1' (str),
                    value (int)
                ]
            ],
    """
    if precinctNum != "all":
        try:
            d = data.ELECTION_DATA[topic]['data'].loc[precinctNum]
        except KeyError as e:
            return jsonify(
                result=False,
                data=None,
                reason=str(e) + " is not a known precinct for this topic")
    else:
        d = data.ELECTION_DATA[topic]['data'].sum()

    return jsonify(
        result=True,
        data=[
            [name, int(vaue)]
            for name, vaue in zip(d.keys(), d.values)
        ]
    )


@app.route('/api/<topic>/<precinctNum>/valid')
def topic_valid(topic, precinctNum):
    """
    """
    d = list(data.ELECTION_DATA[topic]['data'].index.values)
    if precinctNum != "all":
        return jsonify(
            result=True,
            data=precinctNum in d
        )
    else:
        return jsonify(
            result=True,
            data=d
        )


# @app.route('/api/<topic>/<precinctNum>/diff')
# def topic_diff(topic, precinctNum):

#     if precinctNum != "all":
#         d = data.ELECTION_DATA[topic]['data'].loc[precinctNum]
#     else:
#         d = data.ELECTION_DATA[topic]['data'].sum()

#     return jsonify(
#         result=True,
#         data=[
#             [name, int(vaue)]
#             for name, vaue in zip(d.keys(), d.values)
#         ]
#     )


@app.route('/api/<topic>/<precinctNum>/meta')
def topic_meta(topic, precinctNum):
    """
        Return meta data about each precinct's election result

        output:
            {
                "percentTurnout": num,
                "registeredVoters": num,
                "totalVotes": num
            },
    """
    if precinctNum != 'all':
        return jsonify(
            result=True,
            data=data.ELECTION_DATA[topic]['meta'][precinctNum]
        )
    else:
        return jsonify(
            result=True,
            data=data.ELECTION_DATA[topic]['meta']
        )
