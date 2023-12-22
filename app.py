from flask import Flask, render_template, request, redirect
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    try:
        raise Exception("this is the made up exception...")
    except Exception as e:
        housing_error = HousingException(e, sys)
        logging.info(housing_error.error_message)
    return 'Flask App is up and running!'


if __name__ == '__main__':
    app.run(debug=True)
