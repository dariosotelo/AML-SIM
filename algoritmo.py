#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:29:21 2023

@author: darios
"""

##-----------Librerías y lectura de los datos-------------------------

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


data = pd.read_csv("AML-SIM_2/bank_mixed/transactions.csv")


##-----------clase nodo------------------------------------------------

class Nodo:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.siguientes = []

    def __str__(self):
        return str(self.cantidad)

    def agrega(self, *nodos):
        self.siguientes.extend(nodos)

    @staticmethod
    def visualizar(nodes):
        G = nx.DiGraph()
        for node in nodes:
            node._build_graph(G)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
        plt.title("Lista Enlazada")
        plt.show()

    def _build_graph(self, G):
        G.add_node(str(self))
        for siguiente in self.siguientes:
            G.add_edge(str(self), str(siguiente))
            siguiente._build_graph(G)


# Ejemplo
# Crear nodos
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(50)

# Enlazar los nodos
nodo1.agrega(nodo2, nodo3, nodo4)

# Visualizar la lista enlazada
nodo1.visualizar([nodo1, nodo5])

