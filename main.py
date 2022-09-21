from untils import *
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def customerFilter():
    city = request.args.get('city') or None
    state = request.args.get('state') or None
    result = filterByCityAndState(city, state)
    return render_template('index.html', customers=result)


@app.route('/countNames', methods=['GET'])
def countNames():
    result = nameCounts()
    return render_template('count.html', items=result)


@app.route('/orderSum', methods=['GET'])
def orders():
    result = ordersSum()
    return render_template('orderSum.html', sum=result[0])
