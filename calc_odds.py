from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/calculate_odds", methods=["GET"])
def hello_world():
    try:
        prev_year_app = request.json['prevYearApplication']
        prev_year_success = request.json['prevYearSuccess']
    except TypeError:
        # raise {{"Expected": "prevYearApplication, prevYearApplication", "Received": request.json.keys()}}
        return {"Expected": "prevYearApplication, prevYearApplication", "Received": request.json.keys()}

    if len(prev_year_app) != len(prev_year_success):
        return {"Error": "Arrays do not match in length"}

    calculated_odds = calculate_odds(prev_year_app, prev_year_success)

    return {"calculated": calculated_odds}


def calculate_odds(prev_app: list[int], prev_success: list[int]) -> list[int]:
    len_n = len(prev_success)
    calculated_odds = [0] * len_n

    # The last category gets placed in the new calculated odds
    calculated_odds[len_n - 1] += (
            prev_app[len_n - 1] - prev_success[len_n - 1])

    # The first placement in calculated_odds is the prev_app first placement
    calculated_odds[0] = prev_app[0]

    for category in range(1, len_n):
        calculated_odds[category] += prev_app[category - 1] - prev_success[
            category - 1]

    return calculated_odds


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=58585)
