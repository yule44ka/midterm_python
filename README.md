# midterm_python
Info about the code:
- /miles?value=<number>: Convert miles to kilometers. Usage: python client.py --m <number>
- /pounds?value=<number>: Convert pounds to kilograms. Usage: python client.py --p <number>
- /fahrenheit?value=<number>: Convert Fahrenheit to Celsius. Usage: python client.py --f <number>
- /convert: Allows multiple elements to be converted at once. 
- /country?value=<country>: Show info about the country. Usage: python client.py --c <country>
Example of usage:
python3 client.py --m 1 --p 2 --f 11 --c 'Russia'

To pull the Docker image from my Docker Hub repository, use the following command:
docker pull yule44ka/server_image:midterm

To run the container, use the following command:
./run_container.sh
