# -*- coding: utf-8 -*-
##############################################################################
# Name : Walden Wang
# UNI : dw2723
# Final Project
# 
# This file contains the main functions of my personal webpage
#
##############################################################################


#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    # return render_template("index.html")
    return render_template("index.html")

#Assignment route
@app.route("/Assignments")
def assignmentpage():
    return render_template("assignment.html")

#Class page route
@app.route("/Classes")
def classpage():
    return render_template("class.html")

#start the server
if __name__ == "__main__":
    app.run()