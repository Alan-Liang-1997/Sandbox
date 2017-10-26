from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def calculate_fahrenheit(celsius=""):
    fahrenheit = (float(celsius) * (9/5)) + 32
    return '{} Celsius  =  {} Fahrenheit'.format(celsius, fahrenheit)


@app.route('/c/<fahrenheit>')
def calculate_celsius(fahrenheit=""):
    celsius =(float(fahrenheit) - 32) * (5/9)
    return '{} Fahrenheit  =  {:1f} Celsius'.format(fahrenheit, celsius)

if __name__ == '__main__':
    app.run()
