from flask import Flask, request, url_for, redirect, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    #print(os.path.dirname(os.path.realpath(__file__)))
    return render_template('main.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resumeDownload')
def resumeDownload():
    path = "static/Resume_Updated_Jan_21st_2021.pdf"
    return send_file(path, as_attachment=True)

@app.route('/comingSoon')
def comingSoon():
    return render_template('comingSoon.html')


if __name__ == "__main__":      #if running from command line, turn on dev mode
    app.run(debug=True)         #dev mode, server updates on own, shows errors
