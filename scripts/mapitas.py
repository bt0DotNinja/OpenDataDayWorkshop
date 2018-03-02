#!/usr/bin/env python3

from geojsonio import display
from shapely.geometry import Polygon
import matplotlib as mpl
import matplotlib.pyplot as plt



def mapa(nombre):
    """Funcion para dibujar mapas para la presentacion"""
    for nom in nombre:
        with open(nom) as f:
            contents = f.read()
            display(contents)

def figura(poli):
    """Funcion para dibujar figuras"""
    x,y = poli.exterior.xy
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_title('Polígono')
