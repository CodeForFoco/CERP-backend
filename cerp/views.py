"""
    The controls all the endpoints
"""
from flask import jsonify, render_template, request
from cerp import app, data
import json


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


@app.route('/api/<topic>/<precinctNum>/diff')
def topic_diff(topic, precinctNum):
    comp1 = request.args.get('comp1', 'YES/FOR')
    comp2 = request.args.get('comp2', 'NO/AGAINST')

    if precinctNum != 'all':
        d = data.ELECTION_DATA[topic]['data'].loc[precinctNum]
        diff_data = (-1 * d[comp1]) + d[comp2]
        return jsonify(result=True, data=int(diff_data))

    d = data.ELECTION_DATA[topic]['data']
    diff_data = d[[comp1, comp2]].copy()
    diff_data['diff'] = diff_data.apply(
        lambda row: (-1 * row[comp1]) + row[comp2],
        axis=1
    )
    diff_data = diff_data[['diff']].copy()
    return jsonify(result=True, data=json.loads(diff_data.to_json())['diff'])
    
@app.route('/api/<topic>/<precinctNum>/relativeDiff')
def topic_relativeDiff(topic, precinctNum):
    step, diff_data = prepare_heatmap(topic, precinctNum, request)
    return jsonify(result=True, step=step, data=diff_data)

def prepare_heatmap(topic, precinctNum, request):
    comp1 = request.args.get('comp1', 'YES/FOR')
    comp2 = request.args.get('comp2', 'NO/AGAINST')

    if precinctNum != 'all':
        d = data.ELECTION_DATA[topic]['data'].loc[precinctNum]
        diff_data = ((-1 * d[comp1]) + d[comp2])/(d[comp1] + d[comp2])
        return jsonify(result=True, data=int(diff_data))

    d = data.ELECTION_DATA[topic]['data']
    diff_data = d[[comp1, comp2]].copy()
    diff_data['diff'] = diff_data.apply(
        lambda row: ((-1 * row[comp1]) + row[comp2])/(row[comp1] + row[comp2]),
        axis=1
    )
    diff_data = diff_data[['diff']].copy()['diff'].to_dict()
    step = abs(max(max(diff_data.values()), min(diff_data.values()), key=abs))
    step = step/10
    return step, diff_data

@app.route('/api/<topic>/<precinctNum>/heatmap')
def topic_heatmap(topic, precinctNum):
    step, diff_data = prepare_heatmap(topic, precinctNum, request)

    for key, value in diff_data.items():
        diff_data[key] = round(value/step)

    return jsonify(result=True, step=step, data=diff_data)

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
