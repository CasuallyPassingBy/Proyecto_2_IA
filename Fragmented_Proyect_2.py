'''
    Proyecto: Proyecto 2º Parcial: Busquedas Informadas
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Alejandro Laphond Payan
    Mauricio Moscoso Mandujano
    Fernando Ruiz de Huidobro Zapata
    26-abril-2023
    version 0.01

    El presente codigo calcula la distancia euclideana entre dos ciudades 
    de los Estados Unidos Mexicanos, utilizando las coordenadas geograficas 
    de un par de ciudades. Esta distancia es utilizada para obtener los
    valores de la heuristica para el proyecto del 2do Parcial de la materia.
    
    Una vez que se ha obtenido el valor de la heurística del proyecto, el programa le pregunta al usuario que algoritmo 
    de busqueda informada quiere utilizar. Una vez que el usuario decide que algóritmo usar, el codigo lo ejecuta y muestra
    los datos pertinentes de cada uno de los algoritmos

    Ejecucion del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python Proyecto_2_IA.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
    
    Entradas:
        1) El nombre de una ciudad en Mexico que deseemos sea el destino y la ciudad a partir de la cual deseamos empezar la busqueda.
    
    Salidas:
        1) Imprime el arbol de busqueda procesado tomando en cuenta la heurística. Dependiendo del algoritmo que el usuario el camino y los datos 
        particulares de cada algoritmo. Muestra el tiempo de ejecución de cada algoritmo y muestra error si es que aparece uno.
'''
###############################
###############################
##### Dependencias #####
import math, random, Hill_Climbing, Global_constants
from Proyecto_2 import haversine_heuristic
from a_star_unidirectional import (generate_unidirectional_weights,
                                   a_star,
                                    generate_states,
                                    formed_graph,
                                    h_sld)
def heuristic(origin, goal):
    return h_sld[origin]
tree = generate_states(formed_graph)
undirectional_tree = generate_unidirectional_weights(tree)
GOAL = "Bucarest"
for start in h_sld.keys():
    print(start)
    print(Hill_Climbing.Steepest(undirectional_tree, start, GOAL, heuristic))
    print(Hill_Climbing.Stochastic(undirectional_tree, start, GOAL, heuristic))
    print(a_star(undirectional_tree, start, GOAL))
