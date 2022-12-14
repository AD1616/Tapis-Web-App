from py2neo import Graph, Node, Relationship
from py2neo import GraphService
import pandas as pd

def stringFormatter(original):
    return "\"" + original + "\""

def findComponent(component, graph):
    component = stringFormatter(component)
    query = f"MATCH(n:COMPONENT) WHERE n.name CONTAINS {component} RETURN n.name LIMIT 8"
    graph.run(query)
    return graph.run(query).to_data_frame()

def createComponent(component, graph):
    pass

