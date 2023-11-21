# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:51:56 2023

@author: luis mercado
"""

import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key, path=None):
        if path is None:
            path = []
        if node is None:
            return False, path
        path.append(node.key)
        if key == node.key:
            return True, path
        if key < node.key:
            return self._search(node.left, key, path)
        return self._search(node.right, key, path)

def visualize_tree(root):
    G = nx.Graph()
    visualize_tree_helper(root, G)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="red")
    plt.title("Árbol Binario de Búsqueda")
    plt.show()

def visualize_tree_helper(node, G):
    if node:
        if node.left:
            G.add_edge(node.key, node.left.key)
            visualize_tree_helper(node.left, G)
        if node.right:
            G.add_edge(node.key, node.right.key)
            visualize_tree_helper(node.right, G)

def insertar_palabra():
    palabra_insertar = entrada.get()
    bst.insert(palabra_insertar)
    visualize_tree(bst.root)
    resultado.config(text=f"'{palabra_insertar}' insertado en el árbol")

def eliminar_palabra():
    palabra_eliminar = entrada.get()
    encontrado, _ = bst.search(palabra_eliminar)
    if encontrado:
        bst.root = eliminar_nodo(bst.root, palabra_eliminar)
        visualize_tree(bst.root)
        resultado.config(text=f"'{palabra_eliminar}' eliminado del árbol")
    else:
        resultado.config(text=f"'{palabra_eliminar}' no encontrado en el árbol")

def limpiar_arbol():
    bst.root = None
    resultado.config(text="Árbol limpiado")
    visualize_tree(bst.root)

def ejecutar_operacion():
    operacion_seleccionada = opciones.get()
    resultado_operacion.config(text=f"Operación seleccionada: {operacion_seleccionada}")

def crear_menu_operaciones():
    etiqueta_operacion = tk.Label(ventana, text="Selecciona una operación:")
    etiqueta_operacion.pack()

    opciones = ttk.Combobox(ventana, values=operaciones)
    opciones.pack()

    boton_ejecutar = ttk.Button(ventana, text="Ejecutar Operación", command=ejecutar_operacion)
    boton_ejecutar.pack()

    resultado_operacion = tk.Label(ventana, text="")
    resultado_operacion.pack()

def eliminar_nodo(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = eliminar_nodo(root.left, key)
    elif key > root.key:
        root.right = eliminar_nodo(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = eliminar_nodo(root.right, temp.key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Lista de operaciones
operaciones = [
    "Mover un valor entre ubicaciones de memoria o registros",
    "Sumar dos registros o una ubicación de memoria y un registro",
    "Restar dos registros o una ubicación de memoria y un registro",
    # Agrega aquí todas las operaciones que mencionaste
    "Generar una interrupción para una operación del sistema"
]

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Árbol Binario de Búsqueda y Operaciones de Bajo Nivel")

# Elementos de la interfaz gráfica
etiqueta = tk.Label(ventana, text="Palabra a buscar:")
entrada = ttk.Entry(ventana)
boton_buscar = ttk.Button(ventana, text="Buscar")
resultado = tk.Label(ventana, text="")

# Empaquetar elementos en la ventana
etiqueta.pack()
entrada.pack()
boton_buscar.pack()
resultado.pack()

# Crear árbol binario con palabras reservadas
bst = BinarySearchTree()
palabras_reservadas = ["if", "else", "for", "while", "if else", "float", "return", "break", "continue", "switch"]
for palabra in palabras_reservadas:
    bst.insert(palabra)

# Llamar a la función para crear el menú de operaciones
crear_menu_operaciones()

ventana.mainloop()
