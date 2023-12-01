import requests
import argparse

def get_help():
    url = 'http://127.0.0.1:6000/help'
    response = requests.get(url)
    print('/help:', response.text)


def convert_miles(value):
    url = f'http://127.0.0.1:6000/miles?value={value}'
    response = requests.get(url)
    print('/miles:', response.text)


def convert_pounds(value):
    url = f'http://127.0.0.1:6000/pounds?value={value}'
    response = requests.get(url)
    print('/pounds:', response.text)


def convert_fahrenheit(value):
    url = f'http://127.0.0.1:6000/fahrenheit?value={value}'
    response = requests.get(url)
    print('/fahrenheit:', response.text)


def convert_multiple(values):
    url = 'http://127.0.0.1:6000/convert'
    data = {'values': values}
    response = requests.post(url, json=data)
    print('/convert:', response.text)


def country(country_name):
    url = f'http://127.0.0.1:6000/country/{country_name}'
    response = requests.get(url)
    print(response.text)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=float, help='Value for conversion miles', default=0)
    parser.add_argument('--p', type=float, help='Value for conversion pounds', default=0)
    parser.add_argument('--f', type=float, help='Value for conversion fahrenheit', default=0)
    parser.add_argument('--h', action='store_true', help='Get help')
    parser.add_argument('--c', type=str, help='Information about the country', default='')
    return parser.parse_args()


def main():
    args = get_args()
    if args.h:
        get_help()
    if args.m:
        convert_miles(args.m)
    if args.p:
        convert_pounds(args.p)
    if args.f:
        convert_fahrenheit(args.f)
    if args.c:
        country(args.c)

    convert_multiple(['20m', '10p', '100F'])
    convert_multiple(['1m', '100p', '32F'])
    convert_multiple(['1m', '2p', '3F'])


if __name__ == "__main__":
    main()