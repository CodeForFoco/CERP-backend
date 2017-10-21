"""
    The controls all the API endpoints
"""
from flask import jsonify
from api import app, data


@app.route('/')
def index():
    """ If someone hits root dir, show them all paths """
    output = sorted([str(rule) for rule in app.url_map.iter_rules()])
    return jsonify(result=True, paths=output)


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
