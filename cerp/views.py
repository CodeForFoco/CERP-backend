"""
    The controls all the API endpoints
"""
import json
from flask import jsonify, render_template
from cerp import app, data


@app.route('/')
def index():
    """ If someone hits root dir, show them all paths """
    # output = sorted([str(rule) for rule in app.url_map.iter_rules()])
    # return jsonify(result=True, paths=output)
    return render_template('index.html')


@app.route('/presidential/<precinctNum>/pie')
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
    print(data.PRESIDENTIAL_ELECTION_CANADITS_16.head())
    d = data.PRESIDENTIAL_ELECTION_CANADITS_16.loc[int(precinctNum)]

    return jsonify(
        result=True,
        data=[
            [name, int(vaue)]
            for name, vaue in zip(d.keys(), d.values)
        ]
    )


def colorize(n1, n2):
    if (-1 * n1) + n2 > 0:
        return "#3366cc"
    return "#dc3912"


@app.route('/presidential/all/heatmap')
def presidential_all_heatmap():
    """ """

    prez = data.PRESIDENTIAL_ELECTION_CANADITS_16
    prez = prez[['Trump/Pence', 'Clinton/Kaine']].copy()
    prez['diff'] = prez.apply(
        lambda row: colorize(row['Trump/Pence'], row['Clinton/Kaine']),
        axis=1
    )
    prez = prez[['diff']].copy()
    return jsonify(result=True, data=json.loads(prez.to_json())['diff'])


@app.route('/presidential/all/pie')
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
