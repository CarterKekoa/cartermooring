from flask import Flask, request, url_for, redirect, render_template
import os

app = Flask(__name__)

@app.route('/')
def mainPage():
    #print(os.path.dirname(os.path.realpath(__file__)))
    return render_template('main.html')


if __name__ == "__main__":      #if running from command line, turn on dev mode
    app.run(debug=True)         #dev mode, server updates on own, shows errors
