import os
import pandas as pd
from flask import Flask

app = Flask(__name__)

# Load the data
file_path = os.path.join(os.path.dirname(__file__), 'carbon-footprint-travel-mode.csv')
df = pd.read_csv(file_path)

# Import routes after creating the app instance
from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5100)