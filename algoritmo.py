#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 19:29:21 2023

@author: darios
"""

##-----------Librerías y lectura de los datos----------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


data = pd.read_csv("AML-SIM_2/bank_mixed/transactions.csv")


##-----------clase nodo--------------------------------------------------------

class Nodo:
    def __init__(self, id_cuenta):
        self.id_cuenta = id_cuenta
        self.cantidad = []
        self.beneficiarios = []

    def __str__(self):
        return str(self.id_cuenta)

    def agrega(self, *nodos):
        self.beneficiarios.extend(nodos)
        
    def agrega_transaccion(self, cuenta_beneficiaria, cantidad):
        if cuenta_beneficiaria in self.beneficiarios:
            indice = self.beneficiarios.index(cuenta_beneficiaria)
            self.cantidad[indice]+=cantidad
        else:
            self.cantidad.append(cantidad)
            self.beneficiarios.append(cuenta_beneficiaria)

    @staticmethod
    def visualizar(nodes):
        G = nx.DiGraph()
        for node in nodes:
            node._construye_grafo(G)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
        plt.title("Lista Enlazada")
        plt.show()

    def _construye_grafo(self, G):
        G.add_node(str(self))
        for beneficiario in self.beneficiarios:
            G.add_edge(str(self), str(beneficiario))
            beneficiario._construye_grafo(G)
            
    


# Ejemplo
# Crear nodos
nodo1 = Nodo(1, 10)
nodo2 = Nodo(2, 20)
nodo3 = Nodo(3, 30)
nodo4 = Nodo(4, 40)
nodo5 = Nodo(5, 50)
nodo6 = Nodo(6, 60)

# Enlazar los nodos
nodo1.agrega(nodo2, nodo3, nodo4)
nodo5.agrega(nodo6)

# Visualizar la lista enlazada
Nodo.visualizar([nodo1, nodo5])


##-----------creación de la red con los datos simulados------------------------

#En esta línea de código voy a construir una base de datos con los datos que sí sean de alerta
df_alerta=data[data["is_sar"]==True]


nodos={}
for index, row in data.iterrows():
    nodo_id=row["orig_acct"]
    nodo_cantidad=row["base_amt"]
    nodo_beneficiaria_id=row["bene_acct"]
    if nodo_id not in nodos:
        #Construyo nodo vacio
        nodo = nodo.agrega_transaccion(nodo_beneficiaria_id, nodo_cantidad)
        #agrego a la lista
    else:
        #busco el nodo
        #hago el agrega
        nodo = Nodo(nodo_id, nodo)












































