# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    # return render_template("index.html")
    return render_template("index.html")


@app.route("/Assignments")
def assignmentpage():
    return render_template("assignment.html")

@app.route("/Classes")
def classpage():
    return render_template("class.html")

#start the server
if __name__ == "__main__":
    app.run()