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
    #if nodo_id not in nodos:
        #Construyo nodo vacio
        #nodo = nodo.agrega_transaccion(nodo_beneficiaria_id, nodo_cantidad)
        #agrego a la lista
    #else:
        #busco el nodo
        #hago el agrega
        #nodo = Nodo(nodo_id, nodo)


#%%

from scipy.sparse import coo_matrix
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

#%%
import os
print(os.getcwd())  # Imprimir el directorio de trabajo actual
os.chdir('/ruta/del/directorio')

#%% Usando la librería de grafos de Python

import networkx as nx

data = pd.read_csv("~/Proyectos/AML-Simulation/AML-SIM_2/bank_mixed/transactions.csv")

G = nx.Graph()

G.add_nodes_from(data['orig_acct'])
G.add_nodes_from(data['bene_acct'])

    
for _, row in data.iterrows():
    cuenta_origen = row['orig_acct']
    cuenta_beneficiaria = row['bene_acct']
    cantidad = row['base_amt']

    # Verificar si la arista ya existe y sumar cantidades si es el caso
    if G.has_edge(cuenta_origen, cuenta_beneficiaria):
        edge_data = G.get_edge_data(cuenta_origen, cuenta_beneficiaria)
        cantidad_actual = edge_data['cantidad']
        nueva_cantidad = cantidad_actual + cantidad
        G.add_edge(cuenta_origen, cuenta_beneficiaria, cantidad=nueva_cantidad)
    else:
        G.add_edge(cuenta_origen, cuenta_beneficiaria, cantidad=cantidad)



#%% 

num_nodos = G.number_of_nodes()
num_aristas = G.number_of_edges()

print("Número de nodos:", num_nodos)
print("Número de aristas:", num_aristas)



#%%

nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), with_labels=True, node_color='lightblue', node_size=500)

# Dibuja solo las etiquetas de los nodos
nx.draw_networkx_labels(G, pos=nx.spring_layout(G))

# Muestra el gráfico
plt.axis('off')
plt.show()

#%%

pos = nx.spring_layout(G)

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos=pos, node_color='lightblue', node_size=500)

# Dibujar las aristas
nx.draw_networkx_edges(G, pos=pos, edge_color='black')

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos=pos)

# Configurar el diseño del grafo
plt.title('Red de nodos')
plt.axis('off')

# Mostrar el grafo
plt.show()

#%%

pos = nx.spring_layout(G)  # Posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
plt.show()

#%%

import networkx as nx
import plotly.graph_objects as go

fig = go.Figure()
pos = nx.spring_layout(G)

# Crear la figura de Plotly
fig = go.Figure()

# Agregar los nodos a la figura
for node in G.nodes:
    x, y = pos[node]  # Obtener la posición del nodo
    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers', marker=dict(size=10, color='lightblue'), name=str(node)))

# Agregar las aristas a la figura
for edge in G.edges:
    x0, y0 = pos[edge[0]]  # Obtener la posición del primer nodo de la arista
    x1, y1 = pos[edge[1]]  # Obtener la posición del segundo nodo de la arista
    fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(width=1, color='black'), showlegend=False))

# Configurar el diseño de la figura
fig.update_layout(title='Red de nodos', showlegend=False, hovermode='closest')

# Mostrar la figura
fig.show()























