from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('main.html')


if __name__ == "__main__":      #if running from command line, turn on dev mode
    app.run(debug=True)         #dev mode, server updates on own, shows errors
