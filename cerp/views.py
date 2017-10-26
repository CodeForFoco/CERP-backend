"""
    The controls all the endpoints
"""
import json
from flask import jsonify, render_template
from cerp import app, data


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


@app.route('/api/presidential/<precinctNum>/pie')
def presidential_precinct_pie(precinctNum):
    """
        Generate a highcharts pie friendly dataset for each precient

        output:
            [
                [
                    'Trump/Pence' (str),
                    value (int)
                ],
                [
                    'Clinton/Kaine' (str),
                    value (int)
                ]
            ],
    """
    d = data.PRESIDENTIAL_ELECTION_CANADITS_16.loc[precinctNum]

    return jsonify(
        result=True,
        data=[
            [name, int(vaue)]
            for name, vaue in zip(d.keys(), d.values)
        ]
    )


def colorize(n1, n2):
    """
        Returns the color for each diff, based on who got more votes.
        Needs to be expaned to use a color range
    """
    if (-1 * n1) + n2 > 0:
        return "#3366cc"
    return "#dc3912"


@app.route('/api/presidential/all/heatmap')
def presidential_all_heatmap():
    """
        Returns an object containing each of the precents and their color:
        data: {
            precent: color,
            precent: color,
            ...
        }
    """

    prez = data.PRESIDENTIAL_ELECTION_CANADITS_16
    prez = prez[['Trump/Pence', 'Clinton/Kaine']].copy()
    prez['diff'] = prez.apply(
        lambda row: colorize(row['Trump/Pence'], row['Clinton/Kaine']),
        axis=1
    )
    prez = prez[['diff']].copy()
    return jsonify(result=True, data=json.loads(prez.to_json())['diff'])


@app.route('/api/presidential/all/diff')  # if used, change to heatmap
def presidential_all_diff():
    """
        Returns an object containing each of the precents and their color:
        data: {
            precent: diff,
            precent: diff,
            ...
        }
    """

    prez = data.PRESIDENTIAL_ELECTION_CANADITS_16
    prez = prez[['Trump/Pence', 'Clinton/Kaine']].copy()
    prez['diff'] = prez.apply(
        lambda row: (-1 * row['Trump/Pence']) + row['Clinton/Kaine'],
        axis=1
    )
    prez = prez[['diff']].copy()
    return jsonify(result=True, data=json.loads(prez.to_json())['diff'])


@app.route('/api/presidential/all/pie')
def presidential_all_pie():
    """
        Generate a highcharts pie friendly dataset for all precients (sum)

        output:
            [
                [
                    'Trump/Pence' (str),
                    value (int)
                ],
                [
                    'Clinton/Kaine' (str),
                    value (int)
                ]
            ]
    """
    prez = data.PRESIDENTIAL_ELECTION_CANADITS_16
    prez = prez[['Trump/Pence', 'Clinton/Kaine']].copy()
    prez = prez.sum()  # prez is now a series

    return jsonify(
        result=True,
        data=[
            [name, int(vaue)]
            for name, vaue in zip(prez.keys(), prez.values)
        ]
    )
