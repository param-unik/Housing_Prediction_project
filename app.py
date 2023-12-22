from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    return 'Flask App is up and running!'


if __name__ == '__main__':
    app.run(debug=True)
