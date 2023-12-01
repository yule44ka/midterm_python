import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/help', methods=['GET'])
def help():
    help_text = """
    Available conversions:
    - /miles?value=<number>: Convert miles to kilometers. Usage: python client.py --m <number>
    - /pounds?value=<number>: Convert pounds to kilograms. Usage: python client.py --p <number>
    - /fahrenheit?value=<number>: Convert Fahrenheit to Celsius. Usage: python client.py --f <number>
    - /convert: Allows multiple elements to be converted at once. 
    - /country?value=<country>: Show info about the country. Usage: python client.py --c <country>
    """
    return help_text


@app.route('/miles', methods=['GET'])
def convert_miles():
    miles = float(request.args.get('value', 0))
    km_in_mile = 1.60934
    km = miles * km_in_mile
    return str(km)


@app.route('/pounds', methods=['GET'])
def convert_pounds():
    pounds = float(request.args.get('value', 0))
    kg_in_pound = 0.453592
    kg = pounds * kg_in_pound
    return str(kg)


@app.route('/fahrenheit', methods=['GET'])
def convert_fahrenheit():
    far = float(request.args.get('value', 0))
    c = (far - 32) * 5/9
    return str(c)

@app.route('/country/<string:country_name>', methods=['GET'])
def country(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    data = response.json()
    country_data = data[0]
    result = {}
    result["capital"] = country_data["capital"]
    result["flags"] = country_data["flags"]
    result["area"] = country_data["area"]
    return result


@app.route('/convert', methods=['POST'])
def convert_multiple():
    data = request.json
    values = data.get('values', [])
    converted_values = {}

    for value in values:
        if 'm' in value:
            miles = float(value.replace('m', ''))
            km_in_mile = 1.60934
            converted_values[value] = miles * km_in_mile

        elif 'p' in value:
            pounds = float(value.replace('p', ''))
            kg_in_pound = 0.453592
            converted_values[value] = pounds * kg_in_pound

        elif 'F' in value:
            far = float(value.replace('F', ''))
            converted_values[value] = (far - 32) * 5/9

    return jsonify(converted_values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)