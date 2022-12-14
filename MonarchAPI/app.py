from crypt import methods
import flask
from flask import request
import pandas as pd
from datetime import datetime as dt

data = pd.read_csv('data.csv', names=['s','e','m']).set_index('m')

series = pd.Series(index=range(data.s.min(), dt.now().year + 1))    #This creates an empty padas series, starting from first year up until this year.
for m in data.index:
    series.loc[data.loc[m].s:data.loc[m].e] = m #Each year when the monarch is raining the year is going to be there.




app = flask.Flask(__name__)

app.route('/', methods=['GET'])
def home():
    year = int(request.args['year'])
    try:
        return series.loc[year]
    except KeyError:
        return f'Invalid Input ({series.index.min()} - {series.index.max()})'

