from flask import Flask
app = Flask(__name__)

import pandas as pd
import getpass
from py2neo import Graph, Node, Relationship
from py2neo import GraphService
import neo4jupyter

@app.route('/')
def home():
    host = "bolt+s://catalog.pods.icicle.tapis.io:443"
    username = "catalog"
    password = "3hpnfBio0OJ5sHAF5ZzBUDWz0db90i"
    graph = Graph(host, auth=(username, password))
    query = "MATCH(n:COMPONENT) RETURN n LIMIT 5"
    print(graph.run(query).to_data_frame())
    return ''