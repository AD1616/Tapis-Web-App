from flask import render_template, request, redirect, url_for
from py2neo import Graph, Node, Relationship
from py2neo import GraphService
import pandas as pd

from __init__ import app
from cypher import *


def connectToGraph(host, username, password):
    success = 1
    failure = 0
    global graph
    try:
        graph = Graph(host, auth=(username, password))
        return success
    except:
        return failure

    
@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        host = request.form.get("host")
        username = request.form.get("username")
        password = request.form.get("password")
        if(connectToGraph(host, username, password)):
            return redirect(url_for('componentInput'))
        else:
            return redirect('/')
    return render_template("home.html")

@app.route('/componentInput', methods =["GET", "POST"])
def componentInput():
    if request.method == "POST":
        componentName = request.form.get("component")
        df = findComponent(componentName, graph)
        if (df.empty):
            pass
        else:
            return render_template("ComponentInput.html", tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template("ComponentInput.html")

if __name__ == "__main__":
    app.run(debug=True)


