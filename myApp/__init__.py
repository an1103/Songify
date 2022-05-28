from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = '969322be78269058228237e3'

from myApp import routes